from django import forms

from account.models import Login


class LoginModelForm(forms.ModelForm):
    class Meta:
        model = Login
        exclude = ()

