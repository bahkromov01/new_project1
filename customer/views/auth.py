from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from customer.forms import LoginForm


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
    return render(request, 'auth/logout.html')