from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
from courses.models import Course
from django import forms


class CoursesModelForm(forms.ModelForm):
	class Meta:
		model = Course
		#fields = ['first_name', 'last_name', 'phone_number', 'courses', 'package']
		exclude = ['slug', 'venue_adv']


#def courses_list(request):
#    courses = Course.objects.all()
#    return render(request, 'courses/courses_list.html', {'courses': courses})

class CoursesListView(ListView):
       template_name = 'courses/courses_list.html'
       model = Course


#def course_info(request, course_id):
#    course = get_object_or_404(Course, id=course_id)
#    return render(request, 'courses/courses_details.html', {'course': course})

class CoursesView(DetailView):
	template_name = 'courses/courses_details.html'
	model = Course


def course_edit(request, course_id):
    title = "Course edit item"
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CoursesModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            return redirect('courses_list')
    else:
        form = CoursesModelForm(instance=course)
    return render(request, 'courses/courses_edit.html', {'form': form, 'title': title})


def course_add(request):
    title = "Course add item"
    if request.method == 'POST':
        form = CoursesModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('courses_list')
    else:
        form = CoursesModelForm()
    return render(request, 'courses/courses_edit.html', {'form': form, 'title': title})

def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect('courses_list')
