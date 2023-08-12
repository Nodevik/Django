from django import forms
from .models import User

class register(forms.ModelForm):
    class Meta:
        model = User
       # fields = ['name' , 'password' , 'rpassword']   #both are same
        fields = '__all__'
        # exclude = ['name']       # we want those field is not be selected
        labels = {'name':'Enter Name' ,
                  'password':'Enter Password',
                  'rpassword':'Password(again)'}
        help_text = {'rpassword':'no validation apply on password now.'}
        error_messages = {'name' : {"required":"THIS IS JARURI"}}
        widgets = {'password':forms.PasswordInput ,
                   'rpassword':forms.PasswordInput ,
                   'name':forms.TextInput(attrs={'class':'CLASS1'})} 
        