from django import forms

class register(forms.Form):
    name = forms.CharField(min_length=5 , max_length=15 ,strip=False , empty_value='vikas')

    error_msg = forms.CharField(error_messages= {'required':'This is jaruri'})

    check_box_bool = forms.BooleanField(label='agree' , label_suffix='--')

    roll = forms.IntegerField(max_value=10 , min_value=5 )

    float_field = forms.FloatField(max_value=10 , min_value=5 )

    price = forms.DecimalField(max_value=10 , min_value=5 , max_digits=4 , decimal_places=1)

    email = forms.EmailField()

    password = forms.CharField(widget=forms.PasswordInput())

    coustom_error = forms.CharField()


    # raise coustom errors 
    def clean_coustom_error(self):
        var = self.changed_data['coustom_error']
        if (var) < 4:
            raise forms.ValidationError('this is validation error coustom error')
        return var