from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Personal_Background, Education_Background,Family_Background,Course,Tuition


@login_required
def dashboard(request):
    personal_list = Personal_Background.objects.prefetch_related('education', 'family', 'course', 'tuition')
    return render(request, 'student_list/dashboard.html', {'personal': personal_list})
    

def dash(request):
    return render(request, 'student_list/dash.html')
