from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from courses.models import Course
from django import forms

import logging
logger = logging.getLogger(__name__)


class CoursesModelForm(forms.ModelForm):
	class Meta:
		model = Course
		#fields = ['first_name', 'last_name', 'phone_number', 'courses', 'package']
		exclude = ['slug', 'venue_adv']


class CoursesListView(ListView):
       template_name = 'courses/courses_list.html'
       model = Course


class CoursesDetailView(DetailView):
    template_name = 'courses/courses_details.html'
    model = Course


class CourseCreate(CreateView):
    model = Course
    template_name = 'courses/courses_edit.html'
    form_class = CoursesModelForm
    success_url = reverse_lazy('courses_list')


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/courses_edit.html'
    form_class = CoursesModelForm
    success_url = reverse_lazy('courses_list')


class CourseDelete(DeleteView):
    template_name = 'courses/courses_delete.html'
    model = Course
    success_url = reverse_lazy('courses_list')