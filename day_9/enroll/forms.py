from django import forms

class register(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()