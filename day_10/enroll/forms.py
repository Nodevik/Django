from django import forms

class register(forms.Form):
    name = forms.CharField(help_text='this is help text for name field')
    email = forms.EmailField()
    number = forms.IntegerField()
    key = forms.IntegerField(widget=forms.HiddenInput())