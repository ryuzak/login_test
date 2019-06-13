# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.account_dashboard, name="dashboard"),
    path('login/', views.account_login, name="login"),
    path('logout/', views.account_logout, name="logout"),
]
