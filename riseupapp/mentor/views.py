from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# These views take a web request and provide a response via directing to intended hmtml pages.

# This login_required rule prevents access to any webpage without logging in
@login_required(login_url='login') 

# This view will direct users to view cyber mentors.
def mentor(request):
	mentors = Mentor.objects.all()
	context = {'mentors':mentors}
	return render(request, 'mentor/mentor.html', context)

# This view will direct users to the general guidance and blog page.
@login_required(login_url='login')
def blog(request):
	context = {}
	return render(request, 'mentor/blog.html', context)

# This view will direct users to the cyber career specialisation section of the web application.
@login_required(login_url='login')
def guidance(request):
	context = {}
	return render(request, 'mentor/guidance.html', context)

# This request will allow users to register the details if they want to use the site.
@login_required(login_url='login')
def register(request):
	context = {}
	return render(request, 'mentor/register.html', context)

# This view will allow users to understand the purpose of the site and tips on navigation.
@login_required(login_url='login')
def about(request):
	context = {}
	return render(request, 'mentor/about.html', context)


# Code for users who want to register for the site, details are stored in the backend(admin).
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('about')
	else:	
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account created for ' + user)

				return redirect('login')

		context = {'form':form}
		return render(request, 'mentor/reg.html', context)


# For users who have already registered, can login with their credentials.
def loginPage(request):
		if request.user.is_authenticated:
			return redirect('about')
		else:	
			if request.method == 'POST':
				username = request.POST.get('username')
				password = request.POST.get('password')

				user = authenticate(request, username=username, password=password)

				if user is not None:
					login(request, user)
					return redirect('about')

				else:
					messages.info(request, 'Username or Password is Incorrect')


			context = {}
			return render(request, 'mentor/login.html', context)


# Once user logs out, they will be redirected to the log-in page.
def logoutUser(request):
	logout(request)
	return redirect('login')

