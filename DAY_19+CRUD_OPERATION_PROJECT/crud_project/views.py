from django.shortcuts import render , HttpResponseRedirect
from .forms import StudentRegister
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegister(request.POST)
        if fm.is_valid():
            name  = fm.cleaned_data['name']
            email  = fm.cleaned_data['email']
            password  = fm.cleaned_data['password']
            obj = User(name=name , password=password , email=email)
            obj.save()
            fm = StudentRegister()
    else:
        fm = StudentRegister()
    stu = User.objects.all()
    return render(request , 'add_show.html' ,{'form':fm , 'stu':stu} )


#this function delete data
def delete_data(request , id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#this function help to edit student data
def update_data(request , id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegister(request.POST , instance=pi)
        if fm.is_valid():
            fm.save()
            
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegister(instance=pi)
    return render(request , 'update.html' , {'form':fm})