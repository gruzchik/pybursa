from django.shortcuts import render
from models import Course

# Create your views here.


def courses_list(request):
    courses = Course.objects.all() 
    return render(request, 'courses/list.html', {'courses': courses})

def courses_item(request, course_id):
    course = Course.objects.get(id = course_id)
    return render(request, 'courses/details.html', {'course': course})
