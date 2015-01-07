from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

# Create your views here.
from students.models import Student
from django import forms

import logging
logger = logging.getLogger(__name__)


class StudentForm(forms.Form):
    PACKAGE_CHOICES = (
        ('s', 'Standard'),
        ('g', 'Gold'),
        ('p', 'Platinum')
    )
    student_firstname = forms.CharField(label='Name', max_length=100)
    student_lastname = forms.CharField(label='Last name', max_length=255)
    student_email = forms.EmailField()
    students_phone = forms.CharField(max_length=13)
    student_package = forms.ChoiceField(choices=PACKAGE_CHOICES, widget=forms.RadioSelect)


class StudentModelForm(forms.ModelForm):
	class Meta:
		model = Student
		#fields = ['first_name', 'last_name', 'phone_number', 'courses', 'package']
		exclude = ['dossier']


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html',
                  {'students': students})


def student_info(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_details.html', {'student': student})


def student_edit(request, student_id):
    title = "Student edit item"
    if student_id is None:
        student = Student()
    else:
        student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            logger.info("Student info was edit")
            return redirect('students_list')
        else:
            logger.warning("Student cannot edit")
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/student_edit.html', {'form': form, 'title': title})


def student_add(request):
    title = "Student add item"
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            logger.info("Student has been added")
            return redirect('students_list')
        else:
            logger.warning("Student cannot added")
    else:
        form = StudentModelForm()
    return render(request, 'students/student_edit.html', {'form': form, 'title': title})

def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    logger.info("Student has been removed")
    return redirect('students_list')