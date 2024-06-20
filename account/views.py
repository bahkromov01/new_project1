from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from account.forms import LoginModelForm
from account.models import Login


def login_view(request):
    login_list = Login.objects.all()
    context = {
        'login_list': login_list
    }
    return render(request, 'account/login.html', context)


def add_login(request):
    form = LoginModelForm()
    if request.method == 'POST':
        form = LoginModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    context = {
        'form': form,
    }
    return render(request, 'account/add_login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            user = authenticate(username=username, email=email, password1=password2, password2=password1)
            if user is not None:
                login(request, user)
                return redirect('login_view')
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})
