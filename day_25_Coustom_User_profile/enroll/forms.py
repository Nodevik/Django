from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm password(again)' , widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['email','username']
        

class UserProfileChange(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['email','username','last_login','date_joined']