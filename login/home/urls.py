from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name = "index"),
    path('', views.loginPage, name = "loginPage"),
    path('signup', views.signup, name = "signup"),

    path('logout', views.logout, name = "logout"),



]