# -*- coding: utf-8 -*-
from django.urls import include, path
from . import views_api
urlpatterns = [
    path('list/', views_api.RetreiveUsersAPIView.as_view(), name="account_list"),
    path('create/', views_api.CreateUserAPIView.as_view(), name="user_add_api"),
    path('user/', views_api.RetreiveUpdateUserAPIView.as_view(), name="user_detail_api"),
]
