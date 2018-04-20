from .models import UserProfileInfo
from django import forms
from django.contrib.auth.models import User
from django.core import validators

# create here your custom validators

# create here your forms
class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_picture')

