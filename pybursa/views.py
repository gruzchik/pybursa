from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.utils import translation

from courses.models import Course
from coaches.models import Coach
from students.models import Student
from django.template.loader import render_to_string

import logging
logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    return render(request, 'default.html')

class ContactForm(forms.Form):
    email = forms.EmailField(label=_("Email"))
    coach = forms.ModelChoiceField(label=_("CoachForm"), queryset=Coach.objects.all(),)
    student = forms.ModelChoiceField(label=_("StudentName"), queryset=Student.objects.all(),)
    theme = forms.CharField(label=_("Theme"), max_length=255)
    body = forms.CharField(label=_("Message body"), widget=forms.Textarea)


def contact(request):
    #logger.debug("Logging at DEBUG level")
    #logger.info("Logging at INFO level")
    #logger.warning("Logging at WARNING level")
    #logger.error("Logging at ERROR level")
    print translation.get_language()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            theme = form.cleaned_data['theme']
            body = form.cleaned_data['body']
            coach = form.cleaned_data['coach']
            student = form.cleaned_data['student']
            rendered = render_to_string('contact/form_email.html', {'coach_name': coach.first_name},
                                                                   {'student_name': student.first_name})
            send_mail(theme, body, email, ['ahtyrka@yandex.ru'], fail_silently=False)
            messages.success(request, 'Message was sent')
            logger.info("Message was sent")
            return redirect('contact_us')
        else:
            logger.error("Message didn't sent")
    else:

        form = ContactForm()
    return render(request, 'contact/form.html', {'form': form})