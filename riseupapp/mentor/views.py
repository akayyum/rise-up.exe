from django.shortcuts import render
from .models import *

# Create your views here.

def mentor(request):
	mentors = Mentor.objects.all()
	context = {'mentors':mentors}
	return render(request, 'mentor/mentor.html', context)

def selected(request):
	context = {}
	return render(request, 'mentor/selected.html', context)

def guidance(request):
	context = {}
	return render(request, 'mentor/guidance.html', context)