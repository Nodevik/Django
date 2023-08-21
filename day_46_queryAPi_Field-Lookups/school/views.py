from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    # stu_data = Student.objects.filter(name__exact='nazz')
    # stu_data = Student.objects.filter(name__iexact='nAzz')

    # stu_data = Student.objects.filter(name__contains='zz')
    # stu_data = Student.objects.filter(name__contains='ZZ')

    # stu_data = Student.objects.filter(roll__in=[1,2,3])

    # stu_data = Student.objects.filter(marks__gt = 60)
    # stu_data = Student.objects.filter(marks__lt = 60)
    # stu_data = Student.objects.filter(marks__gte = 60)
    # stu_data = Student.objects.filter(marks__lte = 60)

    # stu_data = Student.objects.filter(name__startswith = 'v')
    stu_data = Student.objects.filter(name__istartswith = 'V')


    print(f'query :')
    print(stu_data.query)
    print('----------------------------------\n')
    return render(request, 'home.html', {'students' : stu_data})