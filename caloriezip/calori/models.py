from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPES = (
            (0, 'CUSTOMER'),
            (1, 'ADMIN'),
    )
    user_type = models.IntegerField(
        choices = USER_TYPES, default=0)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Item(models.Model):
    CATEGORIES = (
            (0, 'Vegetables'),
            (1, 'Fruits'),
            (2, 'Grains'),
            (3, 'Meat And Poultry'),
            (4, 'Fish And Seafood'),
            (5, 'Dairy Foods'),
            (6, 'Beans'),
            (7, 'Nuts'),
    )

    name = models.CharField(unique=True, max_length=30)
    calories = models.FloatField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_global = models.BooleanField(default=True)
    category = models.IntegerField(choices=CATEGORIES, default=0)
    in_grams = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ItemConsumption(models.Model):
    user = models.ForeignKey(User,
        on_delete=models.CASCADE, related_name='user_consumtions')
    item = models.ForeignKey(Item,
        on_delete=models.CASCADE, related_name='items_consumtions')
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.name
    
    @property
    def calories_consumed(self):
        return round(self.amount/100*self.item.calories, 2)
