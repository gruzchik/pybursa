from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from courses.models import Course
from django import forms


class CoursesForm(forms.Form):
    TECHNOLOGY_CHOICE = (('p', 'Python'),
                         ('r', 'Ruby'),
                         ('h', "Php"))
    course_name = forms.CharField(label='Name', max_length=100)
    course_description = forms.CharField(label='Description', max_length=255)
#    course_coach = forms.ModelChoiceField(queryset=Coach.objects.all())
#    course_assistant = forms.ModelChoiceField(queryset=Coach.objects.all())
    course_startdate = forms.DateTimeField()
    course_enddate = forms.DateTimeField()
    course_technology = forms.ChoiceField(choices=TECHNOLOGY_CHOICE, widget=forms.RadioSelect)

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})


def course_info(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/courses_details.html', {'course': course})

def course_edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            course.name = form.cleaned_data['course_name']
            course.description = form.cleaned_data['course_description']
 #           course.coach = form.cleaned_data['course_coach']
 #           course.assistant = form.cleaned_data['course_assistant']
            course.start_date = form.cleaned_data['course_startdate']
            course.end_date = form.cleaned_data['course_enddate']
            course.technology = form.cleaned_data['course_technology']
            course.save()
            # process
            return redirect('course_edit', course_id)
    else:
        form = CoursesForm(initial={'course_name':course.name,
        	                        'course_description':course.description,
                                    #'course_coach':course.coach,
                                    #'course_assistant':course.assistant,
                                    'course_startdate':course.start_date,
                                    'course_enddate':course.end_date,
                                    'course_technology':course.technology,
                                    })
    return render(request, 'courses/courses_edit.html', {'form': form})

#def student_edit(request, student_id):
#    title = "Student edit item"
#    if student_id is None:
#        student = Student()
#    else:
#        student = Student.objects.get(id=student_id)
#    if request.method == 'POST':
#        form = StudentModelForm(request.POST, instance=student)
#        if form.is_valid():
#            student = form.save()
#            return redirect('students_list')
#    else:
#        form = StudentModelForm(instance=student)
#    return render(request, 'students/student_edit.html', {'form': form, 'title': title})


def course_add(request):
    title = "Course add item"
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('courses_list')
    else:
        form = CoursesForm()
    return render(request, 'students/student_edit.html', {'form': form, 'title': title})

def course_delete(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    course.delete()
    return redirect('courses_list')
