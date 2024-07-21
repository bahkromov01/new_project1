from django.urls import path

from customer.views.auth import login_page, logout_user, register, send_email, verify_email_done, \
    verify_email_complete, verify_email
from customer.views.views import CustomersView,add_customer, DeleteCustomerView, EditcustomerView, export_data, \
    verify_email_confirm

urlpatterns = [
    path('customer_list/', CustomersView.as_view(), name='customers'),
    path('add_customer/', add_customer, name='add_customer'),
    path('delete_customer/<int:pk>/delete', DeleteCustomerView.as_view(), name='delete_customer'),
    path('edit_customer/<int:pk>/update', EditcustomerView.as_view(), name='edit_customer'),
    path('login_page/', login_page, name='login'),
    # path('login_phone/', login_phone, name='login_phone'),
    path('logout_user/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('export_data/', export_data, name='export_data'),
    path('send_email/', send_email, name='send_email'),

    # sending massage

    path('verify-email/', verify_email, name='verify_email'),
    path('verify-email/done/', verify_email_done, name='verify-email-done'),
    path('verify-email-confirm/<uidb64>/<token>/', verify_email_confirm, name='verify-email-confirm'),
    path('verify-email/complete/', verify_email_complete, name='verify-email-complete'),

]