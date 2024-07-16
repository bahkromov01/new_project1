from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View

from customer.forms import LoginForm, RegisterModelForm, EmailForm


# def login_page(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('customers')
#     else:
#         form = LoginForm()
#     return render(request, 'auth/login.html', {'form': form})


class LoginPageView(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form}

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            form = LoginForm()
            return render(request, 'auth/login.html', {'form':form})


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
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('customers')
    else:
        form = RegisterModelForm

    return render(request, 'auth/register.html', {form:form})


class SendEmailView(View):
    def get(self, request):
        form = EmailForm()
        context = {'form': form}
        return render(request, 'app/email_send.html', context)

    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email_from = form.cleaned_data['email_from']
            email_to = [form.cleaned_data['email_to']]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email_from, email_to)
                messages.success(request, 'Message sent successfully.')
                return redirect('customers')
            except Exception as e:
                messages.error(request, f'Error sending message: {e}')

        context = {'form': form}
        return render(request, 'app/email_send.html', context)