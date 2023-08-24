from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    # stu_data = Student.vikas.all()
    # stu_data = Student.objects.all()
    stu_data = Student.Custom.all()
    return render(request,'student.html',{'st':stu_data})