from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from coaches.models import Coach
from django import forms


class CoachForm(forms.Form):
    COACH_TYPES = (('Coach', 'Coach'), ('Assistant', 'Assistant'))
    coach_name = forms.CharField(label='Name', max_length=100)
    coach_lastname = forms.CharField(label='Lastname', max_length=255)
    coach_email = forms.EmailField()
    coach_phone = forms.CharField(max_length=13)
    coach_ctype = forms.ChoiceField(choices=COACH_TYPES, widget=forms.RadioSelect)


class CoachModelForm(forms.ModelForm):
	class Meta:
		model = Coach
		#fields = ['first_name', 'last_name', 'phone_number', 'courses', 'package']
		exclude = ['dossier']


class CoachListView(ListView):
       template_name = 'coaches/coach_list.html'
       model = Coach


class CoachDetailView(DetailView):
       template_name = 'coaches/coach_details.html'
       model = Coach


class CoachUpdateView(UpdateView):
    model = Coach
    form_class = CoachModelForm
    template_name = 'coaches/coach_edit.html'
    success_url = reverse_lazy('coaches_list')


class CoachCreate(CreateView):
    model = Coach
    form_class = CoachModelForm
    template_name = 'coaches/coach_edit.html'
    success_url = reverse_lazy('coaches_list')


class CoachDelete(DeleteView):
    model = Coach
    template_name = 'coaches/coach_delete.html'
    success_url = reverse_lazy('coaches_list')