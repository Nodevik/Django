from django import forms

class register(forms.Form):
    name = forms.CharField(help_text='this is help text for name field')
    password = forms.CharField(widget=forms.PasswordInput())
    area = forms.CharField(widget=forms.Textarea())
    box = forms.CharField(widget=forms.CheckboxInput())
    file = forms.CharField(widget=forms.FileInput())
    class_cost = forms.CharField(widget=forms.EmailInput(attrs={"class":"class1 class2"  , "id":"id1"}))
    email = forms.EmailField()
    number = forms.IntegerField()
    key = forms.IntegerField(widget=forms.HiddenInput())