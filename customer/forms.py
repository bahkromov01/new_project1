import datetime

from django import forms
from django.contrib.auth.models import User
from customer.models import Customer
from django.contrib.auth import get_user_model


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ()


User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.get(email=email):
            raise forms.ValidationError('Email Does Not Exist')
        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.data.get('password')
        try:
            user = User.objects.get(email=email)
            print(user)
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
        except User.DoesNotExist:
            raise forms.ValidationError(f'{email} Does Not Exist')
        return password


# class PhoneForm(forms.Form):
#     phone_number = forms.CharField(max_length=100)
#     password1 = forms.CharField(max_length=100)
#
#     def clean_phone_number(self):
#         phone_number = self.data.get('phone_number')
#         if not User.objects.get(phone_number=phone_number):
#             raise forms.ValidationError('Incorrect Password')
#         return phone_number
#
#     def clean_password1(self):
#         phone_number = self.cleaned_data.get('phone_number')
#         password1 = self.data.get('password')
#         try:
#             user = User.objects.get(phone_number=phone_number)
#             print(user)
#             if not user.check_password(password1):
#                 raise forms.ValidationError('Incorrect Password')
#         except User.DoesNotExist:
#             raise forms.ValidationError(f'{phone_number} Does Not Exist')
#         return password1


class RegisterModelForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

    def clean_email(self):
        email = self.data.get('email').lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'The {email} is already registered')
        return email

    def clean_confic_password(self):
        password = self.data.get('password')
        confic_password = self.data.get('confic_password')
        if password != confic_password:
            raise forms.ValidationError('Password error')


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email_from = forms.EmailField()
    email_to = forms.EmailField()


