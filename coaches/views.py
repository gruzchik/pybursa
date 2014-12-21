from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from coaches.models import Coach
from django import forms


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
    title = "Coach edit item"
    coach = Coach.objects.get(id=coach_id)
    if request.method == 'POST':
        form = CoachModelForm(request.POST, instance=coach)
        if form.is_valid():
            coach = form.save()
            return redirect('coaches_list')
    else:
        form = CoachModelForm(instance=coach)
    return render(request, 'coaches/coach_edit.html', {'form': form, 'title': title})


def coach_add(request):
    title = "Coach add item"
    if request.method == 'POST':
        form = CoachModelForm(request.POST)
        if form.is_valid():
            coach = form.save()
            return redirect('coaches_list')
    else:
        form = CoachModelForm()
    return render(request, 'coaches/coach_edit.html', {'form': form, 'title': title})

def coach_delete(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    coach.delete()
    return redirect('coaches_list')
