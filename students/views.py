from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student

# Create your views here.


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def students_item(request, student_id):
    students = Student.objects.get(id=student_id)
    return render(request, 'students/details.html', {'student': students})
