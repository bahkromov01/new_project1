from django.urls import path

from customer.views.auth import login_page, logout_user, register
from customer.views.views import customers, add_customer, delete_customer, edit_customer

urlpatterns = [
    path('customer_list/', customers, name='customers'),
    path('add_customer/', add_customer, name='add_customer'),
    path('delete_customer/<int:pk>/delete', delete_customer, name='delete_customer'),
    path('edit_customer/<int:pk>/update', edit_customer, name='edit_customer'),
    path('login_page/', login_page, name='login'),
    # path('login_phone/', login_phone, name='login_phone'),
    path('logout_user/', logout_user, name='logout'),
    path('register/', register, name='register')
]