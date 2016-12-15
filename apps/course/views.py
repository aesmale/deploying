from django.shortcuts import render, redirect
from .models import Course
from django.db import models

# Create your views here.
def index(request):
    context = {
        'courses' : Course.objects.all()
	}
    return render(request, 'course/index.html', context)

def add_course(request):
    Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def remove_course(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')
