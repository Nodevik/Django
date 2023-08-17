from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    # stu_data = Student.objects.get(pk=1)

    # stu_data = Student.objects.first()
    # stu_data = Student.objects.order_by('name').first()

    # stu_data = Student.objects.last()

    # stu_data = Student.objects.latest('pass_date')

    # stu_data = Student.objects.earliest('pass_date')

    # stu_data = Student.objects.all()
    # print(stu_data.exists())


    #*********************************saving data in one line ************************
    # stu_data = Student.objects.create(name='nazzvik', roll=112 , city='amer' , marks='100' , pass_date='2023-08-07')

    # stu_data, created = Student.objects.get_or_create(name='nazzvik', roll=115 , city='amjer' , marks='100' , pass_date='2023-08-07')
    #   print(f' {created} :')

    
    stu_data = Student.objects.filter(id=1).update(name='updated')

    # bulk_create()               #this help to create bulk data , pre or post save signals not working
    # bulk_update()
    # in;_bulk()              #return data in dict


    #********************* delete ***********
    # stu_data = Student.objects.get(pk=1).delete()                   #delete one
    # stu_data = Student.objects.filter(marks=100).delete()           #delete bulk
    # stu_data = Student.objects.all.delete()                         #delete all


    # stu_data = Student.objects.all()
    # print(stu_data.count())

  
    print(f'query :')
    print(stu_data)
    print('----------------------------------\n')
    return render(request, 'home.html', {'student' : stu_data})