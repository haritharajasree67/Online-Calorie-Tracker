from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("item", views.item, name="item"),
    path("item/consumption/", views.item_consumption, name="item-consumption"),
    path("item/consumption/<int:id>/", views.delete_item_consumption, name="item-consumption"),
    path("item/<int:id>/", views.delete_item, name="item-delete"),
    path("public", views.public, name="public"),
    path("history", views.history, name="public"),
    path("bmi-calculator", views.bmi_calculator, name="public"),
    path("item/reset/", views.reset_data,name="reset_data"),
    path("help", views.help,name="help"),
]


