from django import forms
from .models import User

class StudentRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name' , 'email' , 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Enter Your Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'Enter Your Email'}),
            'password': forms.PasswordInput(render_value=True , attrs={'class':'form-control' , 'placeholder':'Enter Your Password'}),
        }