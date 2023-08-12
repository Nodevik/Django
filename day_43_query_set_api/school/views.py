from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    # stu_data = Student.objects.all()

    # stu_data = Student.objects.filter(marks=100)
    # stu_data = Student.objects.exclude(marks=100)

    # stu_data = Student.objects.order_by('name')                       #accending order
    # stu_data = Student.objects.order_by('-name')                      #decending order
    # stu_data = Student.objects.order_by('?')                      #random order

    # stu_data = Student.objects.order_by('id').reverse()[0:5]

    # stu_data = Student.objects.values()                         #it return dict
    # stu_data = Student.objects.values('name','city')
    stu_data = Student.objects.values_list('id',named=True)                       #it return tuple

    # stu_data = Student.objects.distinct()

    # stu_data = Student.objects.dates('pass_date', 'year')                #it return tuple



    print(f'query :')
    print(stu_data)
    print('----------------------------------\n')
    print(stu_data.query)
    return render(request, 'home.html', {'students' : stu_data})