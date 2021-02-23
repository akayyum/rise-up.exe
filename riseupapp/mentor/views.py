from django.shortcuts import render
from .models import *

# Create your views here.

def mentor(request):
	mentors = Mentor.objects.all()
	context = {'mentors':mentors}
	return render(request, 'mentor/mentor.html', context)

def blog(request):
	context = {}
	return render(request, 'mentor/blog.html', context)

def guidance(request):
	context = {}
	return render(request, 'mentor/guidance.html', context)

def register(request):
	context = {}
	return render(request, 'mentor/register.html', context)
