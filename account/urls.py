from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include

from account.views import login_view, add_login, register

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('add_login/', add_login, name='add_login'),
    path('logouot/', logout, name='logout'),
    path('register/', register, name='register')
]