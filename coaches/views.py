from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from coaches.models import Coach
from django import forms


class CoachForm(forms.Form):
    COACH_TYPES = (('C', 'Coach'), ('A', 'Assistant'))
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


def coaches_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coaches/coach_list.html', {'coaches': coaches})


def coach_info(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    return render(request, 'coaches/coach_details.html', {'coach': coach})


def coach_edit(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            coach.first_name = form.cleaned_data['coach_name']
            coach.last_name = form.cleaned_data['coach_lastname']
            coach.email = form.cleaned_data['coach_email']
            coach.phone_number = form.cleaned_data['coach_phone']
            coach.ctype = form.cleaned_data['coach_ctype']
            coach.save()
            return redirect('coach_edit', coach_id)
    else:
        form = CoachForm(initial={'coach_name':coach.first_name,
        	                        'coach_lastname':coach.last_name,
                                    'coach_email':coach.email,
                                    'coach_phone':coach.phone_number,
                                    'coach_ctype':coach.ctype,
                                    })
    return render(request, 'coaches/coach_edit.html', {'form': form})


#def coach_edit(request, coach_id):
#    title = "Coach edit item"
#    coach = Coach.objects.get(id=coach_id)
#    if request.method == 'POST':
#        form = CoachModelForm(request.POST, instance=coach)
#        if form.is_valid():
#            coach = form.save()
#            return redirect('coaches_list')
#    else:
#        form = CoachModelForm(instance=coach)
#    return render(request, 'coaches/coach_edit.html', {'form': form, 'title': title})


def coach_add(request):
    title = "Coach add item"
    if request.method == 'POST':
        form = CoachModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coaches_list')
    else:
        form = CoachModelForm()
    return render(request, 'coaches/coach_edit.html', {'form': form, 'title': title})

def coach_delete(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    coach.delete()
    return redirect('coaches_list')
