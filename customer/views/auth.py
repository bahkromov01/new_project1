from email.message import EmailMessage
from typing import Any

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View

from confic import settings
from customer.forms import LoginForm, RegisterModelForm, EmailForm
from confic import settings
from customer.tokens import account_activation_token


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('customers')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})


# class LoginPageView(View):
#     def get(self, request):
#         form = LoginForm()
#         context = {'form': form}
#
#     def post(self, request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         else:
#             form = LoginForm()
#             return render(request, 'auth/login.html', {'form':form})


# def login_phone(request):
#     if request.method == 'POST':
#         form = PhoneForm(request.POST)
#         if form.is_valid():
#             phone_number = form.cleaned_data['phone_number']
#             password = form.cleaned_data['password']
#             user = authenticate(request, phone_number=phone_number, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('customers')
#     else:
#         form = PhoneForm
#     return render(request, 'auth/login.html', {'form': form})


def logout_user(request):
    if request.method == 'GET':
        logout(request)
        return redirect('customers')
    return render(request, 'auth/logout.html')


def register(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.is_active = False
            user.set_password(password)
            if not user.is_active:
                current_site = get_current_site(request)
                subject = "Verify Email"
                message = render_to_string('email/verify_email_message.html', {
                    'request': request,
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })

                email = EmailMessage(
                    subject, message, to=[user.email]
                )
                email.content_subtype = 'html'
                email.send()
                user.save()
                return redirect('verify-email-done')
            # sent message
            send_mail('AnonymUser', 'You successfully registered !', settings.DEFAULT_FROM_EMAIL, [user.email],
                      fail_silently=False)
            login(request, user)
            return redirect('customers')
    else:
        form = RegisterModelForm

    return render(request, 'auth/register.html', {'form': form})

# class RegisterDoneView(View):
#     def get(self, request):
#         form = RegisterModelForm()
#         return render(request, 'auth/register.html', {"form": form})
#
#     def post(self, request):
#         form = RegisterModelForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             password = form.cleaned_data['password']
#             user.is_active = False
#             user.set_password(password)
#             if not user.is_active:
#                 current_site = get_current_site(request)
#                 subject = "Verify Email"
#                 message = render_to_string('email/verify_email_message.html', {
#                     'request': request,
#                     'user': user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                     'token': account_activation_token.make_token(user),
#                 })
#
#                 email = EmailMessage(
#                     subject, message, to=[user.email]
#                 )
#                 email.content_subtype = 'html'
#                 email.send()
#                 user.save()
#                 login(request, user)
#                 return redirect('verify-email-done')
#             # sent message
#             send_mail('AnonymUser', 'You successfully registered !', settings.DEFAULT_FROM_EMAIL, [user.email],
#                       fail_silently=False)
#             login(request, user)
#             return redirect('customers')
#         else:
#             form = RegisterModelForm
#
#         return render(request, 'auth/register.html', {'form': form})




def send_email(request):
    sent = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = settings.DEFAULT_FROM_EMAIL
            recipients = form.cleaned_data['recipients']
            send_mail(subject, message, from_email, recipients, fail_silently=False)
            sent = True
    else:
        form = EmailForm()

    return render(request, 'email/email_send.html', {'form': form, 'sent': sent})


def verify_email_done(request):
    return render(request, 'email/verify_email_done.html')


def verify_email_complete(request):
    return render(request, 'email/verify_email_complete.html')


def verify_email(request):
    return render(request, 'email/verify_email.html')