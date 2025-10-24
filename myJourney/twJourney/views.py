from django.shortcuts import render
from .models import Student, Learning_Activity

def index(request):
    student = Student.objects.first()  # assuming one student entry
    activities = Learning_Activity.objects.filter(student=student)
    return render(request, 'index.html', {'student': student, 'activities': activities})


def aboutMe(request):
    student = Student.objects.first()
    return render(request, 'aboutMe.html', {'student': student})
