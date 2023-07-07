from django.shortcuts import render
from enroll.forms import register

# Create your views here.
def home(request):
    fm = register( auto_id=True , label_suffix=" - " , initial={"name" : 'vikas'})
    fm.order_fields(field_order=['email' , 'name'])
    return render(request , 'index.html' , {'form' : fm})