import matplotlib
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.utils import timezone
from django.db.models import F, Sum
from django.contrib.auth import logout

from calori.models import Item, ItemConsumption

User = get_user_model()
matplotlib.use('Agg')


def public(request):
    return render(request, 'public.html')


def help(request):
    return render(request, 'help.html')


def index(request):
    if request.user.is_authenticated:
        return redirect('/home')
    return render(request,'index.html')


def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    items = Item.objects.filter(is_global=True)

    if request.user.user_type == 0:
        context = {
            'object_list': items
        }
        consumptions = ItemConsumption.objects.filter(
            user=request.user, date__date=timezone.now())

        if int(request.GET.get('category', -1)) > -1:
            consumptions = consumptions.filter(item__category=int(request.GET.get('category')))

        context['consumed_list'] = consumptions
        total_calorie = consumptions.values('item__name').annotate(
            calories_consumed=(F('amount') * 1.0/100)*F('item__calories')).aggregate(
            total=Sum('calories_consumed')).get('total')
        if total_calorie:
            context['total_calorie'] = round(total_calorie, 2)
        else:
            context['total_calorie'] = 0
        consumptions_grouped = consumptions.values('item__name').annotate(calories_consumed=Sum(
        (F('amount') * 1.0/100)*F('item__calories')))
        labels = list(consumptions_grouped.values_list('item__name', flat=True))
        sizes = list(consumptions_grouped.values_list('calories_consumed', flat=True))

        fig1 = plt.figure()
        border_width = 0.05 # add_axes takes [left, bottom, width, height]
        ax_size = [0+border_width, 0+border_width, 
                1-2*border_width, 1-2*border_width]
        ax1 = fig1.add_axes(ax_size)
        ax1.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',
                startangle=45)
        ax1.axis('equal')
        plt.savefig(f'media/{request.user.username}_peichart.png', dpi=100)
        context['path'] = f'/media/{request.user.username}_peichart.png'
        return render(request, 'user-home.html', context=context)
    if int(request.GET.get('category', -1)) > -1:
        items = items.filter(category=int(request.GET.get('category')))
    context = {
        'object_list': items
    }
    return render(request,'admin-home.html', context=context)


def history(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    start_date = timezone.now().date()
    end_date = timezone.now().date()
    if request.POST.get('start_date'):
        start_date = datetime.strptime(request.POST.get('start_date'), "%Y-%m-%d")
    if request.POST.get('end_date'):
        end_date = datetime.strptime(request.POST.get('end_date'), "%Y-%m-%d")

    print(start_date)
    print(end_date)

    context = {
        'start_date': start_date.strftime("%Y-%m-%d"),
        'end_date': end_date.strftime("%Y-%m-%d")
    }
    consumptions = ItemConsumption.objects.filter(user=request.user,
        date__date__gte=start_date, date__date__lte=end_date)
    if int(request.POST.get('category', -1)) > -1:
        consumptions = consumptions.filter(item__category=int(request.POST.get('category')))
    context['consumed_list'] = consumptions
    total_calorie = consumptions.values('item__name').annotate(
        calories_consumed=(F('amount') * 1.0/100)*F('item__calories')).aggregate(
        total=Sum('calories_consumed')).get('total')
    if total_calorie:
        context['total_calorie'] = round(total_calorie, 2)
    else:
        context['total_calorie'] = 0
    consumptions_grouped = consumptions.values('item__name').annotate(calories_consumed=Sum(
    (F('amount') * 1.0/100)*F('item__calories')))
    labels = list(consumptions_grouped.values_list('item__name', flat=True))
    sizes = list(consumptions_grouped.values_list('calories_consumed', flat=True))

    fig1 = plt.figure()
    border_width = 0.05 # add_axes takes [left, bottom, width, height]
    ax_size = [0+border_width, 0+border_width, 
            1-2*border_width, 1-2*border_width]
    ax1 = fig1.add_axes(ax_size)
    ax1.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',
            startangle=45)
    ax1.axis('equal')
    plt.savefig(f'media/{request.user.username}_peichart.png', dpi=100)
    context['path'] = f'/media/{request.user.username}_peichart.png'
    return render(request, 'calorie-history.html', context=context)


def bmi_calculator(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'GET':
        return render(request,'bmi-calculator.html')

    age = request.POST.get('age', None)
    gender = request.POST.get('gender', None)
    weight = request.POST.get('weight', None)
    height = request.POST.get('height', None)

    if not(age and gender and weight and height):
        messages.error(request, "Incomplete input")
        return render(request,'bmi-calculator.html')
    
    if not age.isnumeric():
        messages.error(request, "Please enter a valid age")
        return render(request,'bmi-calculator.html')
    if not weight.isnumeric():
        messages.error(request, "Please enter a valid weight")
        return render(request,'bmi-calculator.html')
    if not height.isnumeric():
        messages.error(request, "Please enter a valid height")
        return render(request,'bmi-calculator.html')
    
    context = {}
    if gender == "0":
        result = 88.362 + 13.397*float(weight) + 4.799*float(height) - 5.677*float(age)
    else:
        context["gender"] = 1
        result = 447.593 + 9.247*float(weight) + 3.098*float(height) - 4.330*float(age)
    context['result'] = round(result, 2)
    context['weight'] = weight
    context['height'] = height
    context['age'] = age
    return render(request,'bmi-calculator.html', context=context)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 != password2:
            return render(request,'register.html', {"message":"Password doesn't match"})

        try:
            user = User.objects.create(
                username=email, email=email,
                first_name=first_name, last_name=last_name)
        except IntegrityError:
            messages.error(request, "Email already taken")
            return redirect('/register')
        user.set_password(password1)
        user.save()
        auth.login(request, user)
        return redirect("/home")
    return render(request,'register.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/home")
        else:
            return render(request, 'login.html', {"message":"Invalid user!"})
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def item(request):
    if request.method == 'POST':
        item_name = request.POST['item_name']
        calorie = request.POST['calorie']
        category = request.POST['category']
        
        if not (item_name and calorie.isnumeric() and category):
            messages.error(request, "Please all information.")
            return redirect('/')
        try:
            Item.objects.create(
                name=item_name, calories=calorie, category=round(float(category), 2),
                created_by=request.user, is_global=True)
        except IntegrityError:
            messages.error(request, "Item name need to be unique")
    return redirect('/')


def delete_item(request, id):
    if request.method == 'POST':
        Item.objects.get(id=id).delete()
    return redirect('/')


def delete_item_consumption(request, id):
    try:
        ItemConsumption.objects.get(id=id).delete()
    except Exception as e:
        pass
    return redirect('/')


def item_consumption(request):
    if request.method == 'POST':
        item_id = request.POST['item']
        amount = request.POST['amount']
        if not amount.isnumeric():
            messages.error(request, "Enter a numeric value for amount of consumption")
            return redirect('/home')
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            messages.error(request, "Didn't find the item")
            return redirect('/home')
        ItemConsumption.objects.create(
            user=request.user, item=item, amount=int(float(amount)))
    return redirect('/')


def reset_data(request):
    if request.method == 'POST':
        consumptions = ItemConsumption.objects.filter(
            user=request.user, date__date=timezone.now()).delete()
    return redirect('/')


def generate_sample_data():
    from datetime import datetime, timedelta
    import random
    amounts = [50, 100, 150, 200]
    categories = [0, 1, 2, 3, 4, 5, 6, 7]
    items = Item.objects.all()
    t = timezone.now()
    for i in range(300):
        i = ItemConsumption.objects.create(
            user=request.user, item=random.choice(items), amount=random.choice(amounts),
            category=random.choice(categories))
        i.date = t
        t = t+timedelta(days=1)
        i.save()