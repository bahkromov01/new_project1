from django.urls import path

from customer.views.auth import LoginPageView, logout_user, register, SendEmailView
from customer.views.views import CustomersView, AddCustomerView, DeleteCustomerView, EditcustomerView, export_data

urlpatterns = [
    path('customer_list/', CustomersView.as_view(), name='customers'),
    path('add_customer/', AddCustomerView.as_view(), name='add_customer'),
    path('delete_customer/<int:pk>/delete', DeleteCustomerView.as_view(), name='delete_customer'),
    path('edit_customer/<int:pk>/update', EditcustomerView.as_view(), name='edit_customer'),
    path('login_page/', LoginPageView.as_view(), name='login'),
    # path('login_phone/', login_phone, name='login_phone'),
    path('logout_user/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('export_data/', export_data, name='export_data'),
    path('email_send/', SendEmailView.as_view(), name='email_send')

]