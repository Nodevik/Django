from django import forms
from django.core import validators

      

class register(forms.Form):
    name = forms.CharField(error_messages={'required':'enter your name'})
    password = forms.CharField(widget=forms.PasswordInput(), error_messages={'required':'enter your Password'})
    rpassword = forms.CharField(widget=forms.PasswordInput() , error_messages={'required':'enter your password'})

    def clean(self):
        cleaned_data = super().clean()
        valpassword = self.cleaned_data['password']
        valrpassword = self.cleaned_data['rpassword']
        if valpassword != valrpassword:
            raise forms.ValidationError('Password Not Match !')

