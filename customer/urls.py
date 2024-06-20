from django.contrib import admin
from django.urls import path, include

import customer
from app.views import index, product_detail, add_product
from . import views
from .views import customers, add_customer, delete_customer, edit_customer

urlpatterns = [
    path('customer_list/', customers, name='customers'),
    path('add_customer/', add_customer, name='add_customer'),
    path('delete_customer/<int:pk>/delete', delete_customer, name='delete_customer'),
    path('edit_customer/<int:pk>/update', edit_customer, name='edit_customer')
]