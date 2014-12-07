from django.shortcuts import render
from coaches.models import Coach

# Create your views here.

def coaches_list(request):
    coaches = Coach.objects.all()
    return render(request, "coaches/list.html", {'coaches': coaches})

def coaches_item(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    return render(request, "coaches/details.html", {'coach': coach})
