from django import forms
from django.core import validators

#coustom validators
def start_s(value):
    if value[0] != 's':
        raise forms.ValidationError('start with s')
        

class register(forms.Form):
    name = forms.CharField()

    s_start = forms.CharField(validators=[start_s])

    email = forms.EmailField()

    builtin_validators = forms.CharField(validators=[validators.MaxLengthValidator(10)])

    #complete form validation
    def clean(self):
        cleaned_data = super().clean()
        varname = self.cleaned_data['name']
        if len(varname) < 5:
            raise forms.ValidationError('len must be greater than 5')

        varemail = self.cleaned_data['email']
        if len(varemail) < 15:
            raise forms.ValidationError('len must be greater than 15')