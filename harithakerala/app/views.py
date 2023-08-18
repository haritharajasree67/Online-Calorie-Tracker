from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import district, login, ward, house,duty, house3, harithakaramasena, complaint, applications,  houseallot, wardallot1
from app.models import fee, complainthks, housecollectiondetails, function, foodbalance, requestfood, payment
from app.models import localbody
from app.models import idgen
from django.core.files.storage import FileSystemStorage
from datetime import date, datetime
import datetime
from django.contrib.auth import authenticate
from django.core.mail import send_mail


import requests

def index(request):
    return render(request,'index.html')

def index1(request):
    return render(request,'index2.html')

def login1(request):
    return render(request, 'login1.html')

def registration(request):
    return render(request, 'registration.html')

def adminhome(request):
    if 'uid' not in request.session:
        return render(request,"index2.html")
    else:
        return render(request, 'admin-home.html')
    # if 'admin' not in request.session:
    #     return render(request,"publichome.html")
    # else:
    #     return render(request, 'admin-home.html')
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None and user.is_superuser:
    #         login(request, user)
    #         request.session['admin'] = True
    #         return redirect('adminhome')
    #     else:
            
            




def adddistrict_page(request):
    if 'uid' not in request.session:
        return render(request,"index2.html")
    else:
    
         return render(request, 'adddistrict.html')

def adddistrict1(request):
    if 'uid' not in request.session:
        return render(request,"index2.html")
    else:
        
        if request.method == "POST":
            
            data=idgen.objects.get(id=1)
            f=int(data.did)
            f=f+1
            f1="district_id"+str(f)
                        

            data=district()
            data.district_id=f1
            data.district_name=request.POST.get('districtName')
            data.save()

            data1=idgen.objects.get(id=1)
            data1.did=f
            data1.save()


            data2=login()
            data2.username=f1
            data2.password=request.POST.get('password')
            data2.category="district"
            data2.save()
            return render(request, 'admin-home.html')
    

def removedistrict(request):
    if 'uid' not in request.session:
        return render(request,"index2.html")
    else:
    
        data=district.objects.all()
        return render(request, 'viewdistrict.html', {'d1':data})

def removedistrict1(request, s1):
    if 'uid' not in request.session:
        return render(request,"index2.html")
    else:
   
        data=district.objects.get(district_id=s1)
        data.delete()
        return redirect('/removedistrict')




def addfee(request):
    if 'uid' not in request.session:
        return render(request,"index2.html")
    else:
    
        return render(request, 'addfee.html')

def addfee1(request):
    if 'uid' not in request.session:
        return render(request,"index2.html")
    else:
   
        if request.method == "POST":
                
            data=idgen.objects.get(id=1)
            f=int(data.fee_id)
            f=f+1
            f1="fee_id"+str(f)
                
            data=fee()
            data.fee_id=f1
            data.fee_name=request.POST.get('feeName')
            data.fee_description=request.POST.get('titile')
            data.fee_amount=request.POST.get('amount')
            data.fee_date=request.POST.get('date')
            data.save()

            data1=idgen.objects.get(id=1)
            data1.fee_id=f
            data1.save()
            return render(request, 'admin-home.html')
    

def viewcomplaint(request):
    if 'uid' not in request.session:
        return render(request,"index2.html")
    else:
    
        data=complaint.objects.all()
        return render(request, 'adminviewcomplaint.html', {'d1':data})    


def viewfeeremove(request):
    if 'uid' not in request.session:
        return render(request,"index2.html")
    else:
        data=fee.objects.all()
        return render(request, 'viewfee.html', {'d1':data})

def feeremove(request, s1):
    if 'uid' not in request.session:
        return render(request,"index2.html")
    else:
        data=fee.objects.get(fee_id=s1)
        data.delete()
        return redirect('/viewfeeremove')

def updatefeeview(request):
    if 'uid' not in request.session:
        return render(request,"index2.html")
    else:
        data=fee.objects.all()
        return render(request, "viewupdatefee.html", {'d1':data}) 

def updateviewform(request, r1):
    if 'uid' not in request.session:
        return render(request,"index2.html")
    else:
        data = fee.objects.get(fee_id=r1)
        return render(request, "updatefee.html", {'d1':data})


def updatefee(request,r1):
    if 'uid' not in request.session:
        return render(request,"index2.html")
    else:
        data = fee.objects.get(fee_id=r1)
        if request.method == 'POST':
        
            data.fee_name=request.POST.get('feeName')
            data.fee_description=request.POST.get('titile')
            data.fee_amount=request.POST.get('amount')
            data.fee_date=request.POST.get('date')
            data.save()
            return render (request, 'admin-home.html')
    




def dishome(request):
     if 'lid' not in request.session:
        return render(request,"index2.html")
     else:
        return render(request, 'district-home.html')    


def addlocalbody(request):
    if 'lid' not in request.session:
        return render(request,"index2.html")
    else:
        data1=request.session['lid']
    
        return render(request, 'addlocalbody.html',{'d1':data1})

def addlocalbody1(request):
    if 'lid' not in request.session:
        return render(request,"index2.html")
    else:

        if request.method == "POST":
            
            data=idgen.objects.get(id=1)
            f=int(data.local_id)
            f=f+1
            f1="local_id"+str(f)
            
            data=localbody()
            data.local_id=f1
            data.district_id_id = request.POST.get('sdistrict')
            #  data.local_district=request.POST.get('districtName')
            data.local_name=request.POST.get('name')
            data.local_category=request.POST.get('category')
            data.save()

            data1=idgen.objects.get(id=1)
            data1.local_id=f
            data1.save()

            data2=login()
            data2.username=f1
            data2.password=request.POST.get('password')
            data2.category="localbody"
            data2.save()
            return render(request, 'district-home.html')
    
def removelocalbody(request):
    if 'lid' not in request.session:
        return render(request,"index2.html")
    else:
        data=localbody.objects.all()
        return render(request, 'viewlocalbody.html', {'d1':data})

def removelocalbody1(request, s1):
    if 'lid' not in request.session:
        return render(request,"index2.html")
    else:
        data=localbody.objects.get(local_id=s1)
        data.delete()
        return redirect('/removelocalbody')




def localhome(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        return render(request, 'localbody-home.html')


def addward(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=request.session['wid']
        return render(request, 'addward.html', {'d1':data})


def addward1(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        if request.method == "POST":
            
            data=idgen.objects.get(id=1)
            f=int(data.ward_id)
            f=f+1
            f1="ward_id"+str(f)
                

            data=ward()
            data.ward_id=f1
            data.local_id_id = request.POST.get('localid')
            data.ward_number=request.POST.get('wardNumber')
            data.ward_membername=request.POST.get('wardmembername')
            data.ward_contact=request.POST.get('contactnumber')
            data.ward_email=request.POST.get('email')
            data.save()

            data1=idgen.objects.get(id=1)
            data1.ward_id=f
            data1.save()

            #  data2=login()
            #  data2.username=request.POST.get('email')
            #  data2.password=f1
            #  data2.category="localbody"
            #  data2.save()
            return render(request, 'localbody-home.html')
    
def removeward(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=ward.objects.all()
        return render(request, 'viewward.html', {'d1':data}) 

def removeward1(request, s1):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=ward.objects.get(ward_id=s1)
        data.delete()
        return redirect('/removeward')   
     


def login3(request):
    data=login.objects.all()
    if request.method == 'POST':
        
        username=request.POST.get('username')  
        password=request.POST.get('password')
        flag=0
        for da in data:
            if username==da.username and password==da.password:
                type=da.category
                flag=1
                #request.session['uid']=username
                if type=="admin":
                    request.session['uid']=username
                    return redirect('/adminhome')
                elif type=="district":
                    request.session['lid']=username
                    return redirect('/dishome')
                elif type=="localbody":
                    request.session['wid']=username
                    return redirect('/localhome')
                elif type=="house":
                    request.session['hid']=username
                    return redirect('/househome')
                elif type=="hksemployee":
                    request.session['eid']=username
                    return redirect('/hksemployeehome')
                
                else:
                    return render(request,"login1.html", {'error': "Invalid"})  
                    #return HttpResponse("Invalid")
        if flag==0:
            #return HttpResponse("user doesn't exist")  
            return render(request,"login1.html", {'error': "Invalid username or password"})
    return render(request, 'login1.html')     

def harithakarmasenaemp(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        return render(request, 'harithaksemp.html')

def house1(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=ward.objects.all()
        return render(request, 'addhouse.html', {'d1':data})

def addhouse(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        if request.method == "POST":
                

            data=house3()
            data.house_number = request.POST.get('housenumber')
            data.ward_id_id=request.POST.get('sward')
            data.house_name=request.POST.get('housename')
            data.house_location=request.POST.get('location')
            data.house_ownername=request.POST.get('houseowner')
            data.house_address=request.POST.get('address')
            data.house_aadhar=request.POST.get('aadharnumber')
            data.house_contact=request.POST.get('contactnumber')
            data.house_email=request.POST.get('email')
            data.save()

            data2=login()
            data2.username=request.POST.get('housenumber')
            data2.password=request.POST.get('contactnumber')
            data2.category="house"
            data2.save()

            
            return render(request, 'localbody-home.html')
    
def removehouse(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=house3.objects.all()
        return render(request, 'removehouse.html', {'d1':data}) 

def removehouse1(request, s1):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=house3.objects.get(house_number=s1)
        data.delete()
        return redirect('/removehouse') 


def dutyview(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        return render(request, 'dutymaster.html')

def duty1(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        if request.method == "POST":
         
            data=idgen.objects.get(id=1)
            f=int(data.duty_id)
            f=f+1
            f1="duty_id"+str(f)
                

            data=duty()
            data.duty_id = f1
            data.duty_name = request.POST.get('jobname')
            data.duty_description=request.POST.get('description') 
            data.save()

            data1=idgen.objects.get(id=1)
            data1.duty_id=f
            data1.save()

            
            return render(request, 'localbody-home.html')
        
def removeduty(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=duty.objects.all()
        return render(request, 'viewremoveduty.html', {'d1':data})

def removeduty1(request, s1):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=duty.objects.get(duty_id=s1)
        data.delete()
        return redirect('/removeduty')  

def updatedutyview(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=duty.objects.all()
        return render(request, "viewupdateduty.html", {'d1':data}) 

def updatedutyform(request, r1):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data = duty.objects.get(duty_id=r1)
        return render(request, "updateduty.html", {'d1':data})


def updateduty(request,r1):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data = duty.objects.get(duty_id=r1)
        if request.method == 'POST':
        
            data.duty_name=request.POST.get('jobname')
            data.duty_description=request.POST.get('description')
        
            data.save()
            return render (request, 'localbody-home.html')    



def hksemp(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=ward.objects.all()
        return render(request, 'hksaddemp.html', {'d1':data}) 

def hksemp1(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        if request.method == "POST":
            
            data=idgen.objects.get(id=1)
            f=int(data.hks_id)
            f=f+1
            f1="hks_id"+str(f)
                

            data=harithakaramasena()
            data.hks_id = f1
            data.hks_name = request.POST.get('name')
            data.hks_address=request.POST.get('address') 
            data.hks_gender=request.POST.get('gender') 
            data.hks_age=request.POST.get('age') 
            data.hks_phonenumber=request.POST.get('phonenumber') 
            data.hks_email=request.POST.get('email') 
            data.ward_id_id=request.POST.get('ssward')
            data.hks_date=request.POST.get('date')  
            data.save()

            Photo = request.FILES['sphoto']
            fs = FileSystemStorage()
            filename = fs.save(Photo.name, Photo) 
            uploaded_file_url = fs.url(filename)
            data.hks_photo=uploaded_file_url
            data.save()

            #  data2=login()
            #  data2.username=request.POST.get('email')
            #  data2.password=request.POST.get('phonenumber')
            #  data2.category="hksemployee"
            #  data2.save()


            data1=idgen.objects.get(id=1)
            data1.hks_id=f
            data1.save()

            
            return render(request, 'localbody-home.html')
    
def removehks(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=harithakaramasena.objects.all()
        return render(request, 'removehks.html', {'d1':data})

def removehks1(request, s1):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=harithakaramasena.objects.get(hks_id=s1)
        data.delete()
        return redirect('/removehks')     





def wardhouse(request):
    return render(request, 'wardhousecollection.html') 



def househome(request):
    return render(request, 'house.html')    

def housecomplaint(request):
    data=request.session['hid']
    return render(request, 'housecomplaint.html', {'d1':data})     
    
def housecomplaint1(request):
        if request.method == "POST":
         
         data=idgen.objects.get(id=1)
         f=int(data.cmp_id)
         f=f+1
         f1="complaint_id"+str(f)
             

         data=complaint()
         data.complaint_id = f1
         data.house_number_id = request.POST.get('housenumber')
         data.complaint_complaint=request.POST.get('complaint') 
         data.save()

         data1=idgen.objects.get(id=1)
         data1.cmp_id=f
         data1.save()

        #  return redirect('/househome') 
         return render(request, 'house.html')    


def public(request):
    return render(request, 'publichome.html') 

def application(request):
  
        data1=district.objects.all()
        data=ward.objects.all()
        data2=localbody.objects.all()
        return render(request, 'application.html', {'d1':data, 'd2':data1, 'd3':data2}) 

def application1(request):
  
        if request.method == "POST":
            
            data=idgen.objects.get(id=1)
            f=int(data.request_id)
            f=f+1
            f1="request_id"+str(f)
                

            data=applications()
            data.request_id = f1
            data.request_name = request.POST.get('aname')
            data.request_address = request.POST.get('aaddress')
            data.request_dob = request.POST.get('adob')
            data.request_gender = request.POST.get('agender')
            data.request_age = request.POST.get('aage') 
            data.request_qualification = request.POST.get('qualification')
            data.district_id_id=request.POST.get('ssdistrict')
            data.ward_id_id=request.POST.get('ssward')
            data.local_id_id=request.POST.get('slocalbody')
            data.request_rationcardtype = request.POST.get('rationcardtype')
            data.request_income = request.POST.get('annualincome') 
            data.request_phonenumber = request.POST.get('aphonenumber') 
            data.request_email = request.POST.get('aemail') 
            data.status="Not Registered"   
            data.save()

            Photo = request.FILES['ssphoto']
            fs = FileSystemStorage()
            filename = fs.save(Photo.name, Photo) 
            uploaded_file_url = fs.url(filename)
            data.request_photo=uploaded_file_url
            data.save()

            Photo = request.FILES['saadhar']
            fs = FileSystemStorage()
            filename = fs.save(Photo.name, Photo) 
            uploaded_file_url = fs.url(filename)
            data.request_aadhardcard=uploaded_file_url
            data.save()

            Photo = request.FILES['sincome']
            fs = FileSystemStorage()
            filename = fs.save(Photo.name, Photo) 
            uploaded_file_url = fs.url(filename)
            data.request_inomecertificate=uploaded_file_url
            data.save()
            
            data2=login()
            data2.username=request.POST.get('aemail')
            data2.password=request.POST.get('aphonenumber')
            data2.category="hksemployee"
            data2.save()

            data1=idgen.objects.get(id=1)
            data1.request_id=f
            data1.save()

            
            return render(request, 'index2.html')
    
def viewapplication(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        hk=request.session['wid']
        data=applications.objects.filter(local_id=hk).filter(status="Not Registered")
        return render(request, 'verifyapplication.html', {'d1':data}) 

def acceptharithakarma(request,id):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=applications.objects.get(request_id=id)
        if data.request_income<60000 and data.request_rationcardtype=="BPL":
            data.status="registered"
            data.save()
            data3=idgen.objects.get(id=1)
            f=int(data3.hks_id)
            f=f+1
            f1="hks_id"+str(f)
                    

            data2=harithakaramasena()
            data2.hks_id = f1
            data2.hks_name = data.request_name
            data2.hks_address=data.request_address
            data2.hks_gender=data.request_gender
            data2.hks_age=data.request_age
            data2.hks_phonenumber=data.request_phonenumber
            data2.hks_email=data.request_email
            data2.ward_id_id=data.ward_id_id
            data2.hks_date=date.today()

        

            
            data2.hks_photo=data.request_photo
            data2.save()


            data1=idgen.objects.get(id=1)
            data1.hks_id=f
            data1.save()
            send_mail('alert','Approved your Application','from@example.co',[data.request_email,])

            return render(request,'localbody-home.html')
        else:

            data.status="rejected"
            data.save()
            return render(request,'localbody-home.html')
# else:
#     send_mail('alert','Approved your Application','from@example.co',['haritharajasree@gmail.com'])


# def rejecthraithakarma(request,id):
#     data=applications.objects.get(request_id=id)
#     data.status="rejected"
#     data.save()

    
#     return render(request,'localbody-home.html')

def viewhks(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=harithakaramasena.objects.all()
        return render(request, 'viewhks.html', {'d1':data})


def allotward(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=ward.objects.all()
        return render(request, 'wardallotment.html', {'d1':data})

def allotward1(request,id):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=ward.objects.all()
        data1=duty.objects.all()
        return render(request, 'allotward.html', {'d':data,'d1':data1,'id':id})

def allotward2(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        if request.method == "POST":
            
            data=idgen.objects.get(id=1)
            f=int(data.allot_id)
            f=f+1
            f1="allot_id"+str(f)
                

            data=wardallot1()
            data.allot_id = f1
            data.ward_id_id=request.POST.get('ssward')
            
            data.duty_id_id=request.POST.get('sjob')
            data.starting_date=request.POST.get('sdate') 
            data.ending_date=request.POST.get('edate') 
            
            data.save()

        

            data1=idgen.objects.get(id=1)
            data1.allot_id=f
            data1.save()

            
            return render(request, 'localbody-home.html')
    



    
def allothouse(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=harithakaramasena.objects.all()
        return render(request, 'houseallotment.html', {'d1':data}) 

def allothouse1(request,id):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        data=wardallot1.objects.all()
        data1=house3.objects.all()
    
        return render(request, 'allothouse.html', {'d':data,'d1':data1,  'id':id}) 

def allothouse2(request):
    if 'wid' not in request.session:
        return render(request,"index2.html")
    else:
        if request.method == "POST":
            
            data=idgen.objects.get(id=1)
            f=int(data.allothouse_id)
            f=f+1
            f1="allot_id"+str(f)
                

            data=houseallot()
            data.allothouse_id = f1
            data.hks_id_id=request.POST.get('employeeid')
            data.allot_id_id=request.POST.get('wardss')
            data.house_number_id=request.POST.get('hnumber')
            #  data.starting_housenumber=request.POST.get('hnumber')
            #  data.ending_housenumber=request.POST.get('enumber')
            
            data.save()

        

            data1=idgen.objects.get(id=1)
            data1.allothouse_id=f
            data1.save()

            
            return render(request, 'localbody-home.html')
    


    
def hksemployeehome(request):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        return render(request,'harithaksemphome.html')     
    

def viewwardhks(request):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        hk=request.session['eid']
        data10=harithakaramasena.objects.get(hks_email=hk)
        print("dddddddddddddddddddddddd")
        data=houseallot.objects.filter(hks_id_id=data10.hks_id)
        return render(request, 'viewwardhks.html', {'d1':data}) 

# def hostel_view_transfer_request(request):
#     data10=tbl_student.objects.filter(category='Hostel')
#     data=tbl_transfer_request.objects.filter(status='Approved').filter(student_id_id__in=[ct.student_id for ct in data10])
#     return render(request,"hostel_view_transfer_request.html",{'data':data})


def viewhousehks(request):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        hk=request.session['eid']
        data10=harithakaramasena.objects.get(hks_email=hk)
        
        data=houseallot.objects.filter(hks_id_id=data10.hks_id)
        return render(request, 'viewhousehks.html', {'d1':data})  

def housecollection(request,id):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        data = houseallot.objects.get(allothouse_id=id)
        data1 = duty.objects.all()

        return render(request,'housecollection.html',{'d1':data, 'd2':data1})

def housecollection1(request):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        if request.method == "POST":
            
            data=idgen.objects.get(id=1)
            f=int(data.collection_id)
            f=f+1
            f1="housecollection_id"+str(f)
                

            data=housecollectiondetails()
            data.collection_id = f1
            data.ward_id_id = request.POST.get('wardss')
            data.house_number_id=request.POST.get('houses') 
            data.duty_id_id=request.POST.get('collectionmaterial') 
            
            data.collection_month=request.POST.get('month') 
            data.collection_year=request.POST.get('year') 
            data.collection_date=request.POST.get('date') 
            data.collection_fee=request.POST.get('collectionfee') 
            data.save()

            data1=idgen.objects.get(id=1)
            data1.collection_id=f
            data1.save()
            data3=duty.objects.get(duty_id=request.POST.get ('collectionmaterial'))
            data2=house3.objects.get(house_number=request.POST.get ('houses'))
            send_mail('alert','Month='+data.collection_month+',Date='+data.collection_date+',Fees='+data.collection_fee+',Item='+data3.duty_name,'from@example.co',[data2.house_email,])
            #  return redirect('/househome') 
            return render(request, 'harithaksemphome.html')
        # else: 
        #     send_mail('alert','collection details','from@example.co',['haritharajasree@gmail.com'])


def hkscomplaint(request):
    hk=request.session['eid']
    data=harithakaramasena.objects.get(hks_email=hk)
    return render(request, 'hkscomplaint.html', {'d1':data})     
    
def hkscomplaint1(request):
        if request.method == "POST":
         
         data=idgen.objects.get(id=1)
         f=int(data.cmphks_id)
         f=f+1
         f1="complainthks_id"+str(f)
             

         data=complainthks()
         data.complainthks_id = f1
         data.hks_id_id = request.POST.get('employeeid')
         data.complainthks_complaint=request.POST.get('complainthks') 
         data.save()

         data1=idgen.objects.get(id=1)
         data1.cmphks_id=f
         data1.save()

        #  return redirect('/househome') 
         return render(request, 'harithaksemphome.html')   
        


def functiondetails(request):
    data=request.session['hid']
    data1=house3.objects.get(house_number=data)
    return render(request, 'functiondetail.html', {'d1':data1})
   

def functiondetails1(request):
    if request.method == "POST":
         
         data=idgen.objects.get(id=1)
         f=int(data.function_id)
         f=f+1
         f1="function_id"+str(f)
              

         data=function()
         data.function_id=f1
         data.house_number_id=request.POST.get('housenumber')
         data.ward_id_id=request.POST.get('wardnumber')
         data.function_date=request.POST.get('date')
         data.function_type=request.POST.get('functiontype')
         data.status="pending"
         data.save()

         data1=idgen.objects.get(id=1)
         data1.function_id=f
         data1.save()
         return render(request, 'house.html') 
    
def viewfunctiondetails(request):
    # if 'eid' not in request.session:
    #     return render(request,"index2.html")
    # else:
        hid=request.session['hid']
        data=function.objects.filter(house_number=hid).filter(status="Approved")
        return render(request, 'viewfunctiondetails.html', {'d1':data}) 

 


def foodbalances(request,id):
    data = function.objects.get(function_id=id)   
    return render(request,'foodbalance.html', {'d1':data})  

def foodbalances1(request):
        if request.method == "POST":
         
         data=idgen.objects.get(id=1)
         f=int(data.foodbalance_id)
         f=f+1
         f1="foodbalance_id"+str(f)
              

         data=foodbalance()
         data.foodbalance_id=f1
         data.function_id_id=request.POST.get('functionid')
         data.food_type=request.POST.get('foodtype')
         data.food_quantity=request.POST.get('balancequantity')
         data.food_preparationtime=request.POST.get('preprationtime')
         data.food_usebefore=request.POST.get('usedbefore')
         data.save()

         data1=idgen.objects.get(id=1)
         data1.foodbalance_id=f
         data1.save()
         return render(request, 'house.html')  


    
def housecollectionview(request):
    hid=request.session['hid']
    data=housecollectiondetails.objects.filter(house_number=hid)
    return render(request, 'viewcollectiondetails.html', {'d1':data}) 
         

def viewfunctionhks(request):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        hk=request.session['eid']
        data10=harithakaramasena.objects.get(hks_email=hk)

        # data2=function.objects.filter(status="pending").filter(ward_id_id=data10.ward_id_id)
        data2=function.objects.filter(status="pending")
        return render(request, 'viewfunctionhks.html', {'d1':data2}) 
 
def acceptfunction(request,id):    
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:

        data=function.objects.get(function_id=id)
        data.status="Approved"
        data.save() 
        return redirect('/viewfunctionhks') 

def rejectfunction(request,id):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        data=function.objects.get(function_id=id)
        data.status="Rejected"
        data.save() 
        return redirect('/viewfunctionhks')   
   


def viewfoodbalance(request):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        data1=foodbalance.objects.all()
        return render(request,'viewfooddetails.html',  {'d2':data1}) 

def foodcollectionpoint(request,r1):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        data = foodbalance.objects.get(foodbalance_id=r1)
        
        return render(request,'foodcollectionpoint.html', {'d1':data})  


def foodcollectionpoint1(request,r1):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        data = foodbalance.objects.get(foodbalance_id=r1)
        if request.method == 'POST':
            
            
            data.function_id_id=request.POST.get('functionid')
            data.food_type=request.POST.get('foodtype')
            data.food_quantity=request.POST.get('balancequantity')
            data.food_preparationtime=request.POST.get('preprationtime')
            data.food_usebefore=request.POST.get('usedbefore')
            data.food_collectionpoint=request.POST.get('collectionpoint')
            data.save()

            return render(request, 'harithaksemphome.html')      


def viewfoodbalancerequest(request):
    data=foodbalance.objects.all()
    return render(request, 'viewfoodrequest.html', {'d1':data}) 

def foodrequest(request,id):
    hid=request.session['hid']
    data1=house3.objects.get(house_number=hid)
    data2=datetime.datetime.now().strftime ("%Y-%m-%d")
    data3=datetime.datetime.now().strftime('%H:%M:%S')
    data = foodbalance.objects.get(foodbalance_id=id) 
    
    return render(request, 'foodrequest.html', {'d1':data, 'd2':data1, 'data2':data2, 'data3':data3}) 

def foodrequest1(request):
        if request.method == "POST":
         
         data=idgen.objects.get(id=1)
         f=int(data.foodrequest_id)
         f=f+1
         f1="request_id"+str(f)
              

         data=requestfood()
         data.foodrequest_id=f1
         data.foodbalance_id_id_id=request.POST.get('foodid')
         data.house_number_id=request.POST.get('housenumber')
         data.request_time=request.POST.get('time')
         data.request_date=request.POST.get('date')
         data.status="pending"
         
         data.save()

         data1=idgen.objects.get(id=1)
         data1.foodrequest_id=f
         data1.save()
         return render(request, 'house.html')  
        
def viewfoodrequest(request):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        data1=requestfood.objects.filter(status="pending")
        return render(request,'viewrequest.html',  {'d1':data1})

def acceptfoodrequest(request,id):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        data=requestfood.objects.get(foodrequest_id=id)
        data.status="Approved"
        data.save() 
        return redirect('/viewfoodrequest') 

def rejectfoodrequest(request,id):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        data=requestfood.objects.get(foodrequest_id=id)
        data.status="Rejected"
        data.save() 
        return redirect('/viewfoodrequest')           




def houseowner(request):
    return render(request,'houseowner.html') 

def viewrequestlocalbody(request):
    data=harithakaramasena.objects.all()
    return render(request, 'viewrequestlocalbody.html', {'d1':data}) 

def viewrequestward(request,id):
    data=wardallot1.objects.filter(hks_id_id=id)
    return render(request, 'viewrequestward.html', {'d1':data}) 

def viewrequesthouse(request,id):
    data=houseallot.objects.filter(hks_id_id=id)
    return render(request, 'viewrequesthouse.html', {'d1':data}) 

def viewhousepayment(request):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
    # hid=request.session['hid']
        data=housecollectiondetails.objects.all()
        return render(request, 'viewhousepayment.html', {'d1':data}) 

def payments(request,id):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        eid=request.session['eid']
        data=harithakaramasena.objects.get(hks_email=eid)
        data1=datetime.datetime.now().strftime ("%Y-%m-%d")
        data2 = housecollectiondetails.objects.get(collection_id=id) 
        return render(request, 'payment.html',{'d1':data, 'd2':data1, 'd3':data2}) 

def payment1(request):
    if 'eid' not in request.session:
        return render(request,"index2.html")
    else:
        if request.method == "POST":
         
         data=idgen.objects.get(id=1)
         f=int(data.payment_id)
         f=f+1
         f1="payment_id"+str(f)
              

         data=payment()
         data.payment_id=f1
         data.hks_id_id=request.POST.get('hksid')
         data.house_number_id=request.POST.get('housenumber')
        #  data.duty_id_id=request.POST.get('material')
         data.payment_month=request.POST.get('month')
         data.payment_date=request.POST.get('paymentdate')
         data.payment_amount=request.POST.get('amount')
        data.payment_sack=request.POST.get('sack')
        data.payment_finalamount=request.POST.get('amountpaid')
        #  data.status="pending"
         
        data.save()

        data1=idgen.objects.get(id=1)
        data1.payment_id=f
        data1.save()
        return render(request, 'harithaksemphome.html')  
        

def viewfunctiondetailscollections(request):
    hid=request.session['hid']
    data=function.objects.filter(house_number=hid).filter(status="Approved")
    return render(request, 'viewfunctiondetailscollections.html', {'d1':data})   


def viewcollectionpointhouse(request,id):
    # hid=request.session['hid']
    # data=function.objects.filter(house_number=hid)
    data1=foodbalance.objects.filter(function_id=id)
    return render(request, 'viewfoodcollectionpoint.html', {'d1':data1})       

def adminreport(request):
    data=district.objects.all()
    return render(request, 'adminreport.html', {'d1':data})


# def adminlogout(request):
#     del request.session['admin']
#     return render(request,"public.html")

def sample(request):
    return render(request,"sample.html")


def adminlogout(request):
    del request.session['uid']
    return render(request,"index2.html")   

def districtlogout(request):
    del request.session['lid']
    return render(request,"index2.html")        

def localbodylogout(request):
    del request.session['wid']
    return render(request,"index2.html")  

def hkslogout(request):
    del request.session['eid']
    return render(request,"index2.html")      

  
      
     

        

# Create your views here.

