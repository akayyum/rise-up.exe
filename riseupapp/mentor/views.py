from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def mentor(request):
	mentors = Mentor.objects.all()
	context = {'mentors':mentors}
	return render(request, 'mentor/mentor.html', context)

@login_required(login_url='login')
def blog(request):
	context = {}
	return render(request, 'mentor/blog.html', context)

@login_required(login_url='login')
def guidance(request):
	context = {}
	return render(request, 'mentor/guidance.html', context)

@login_required(login_url='login')
def register(request):
	context = {}
	return render(request, 'mentor/register.html', context)



def registerPage(request):
	if request.user.is_authenticated:
		return redirect('mentor')
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



def loginPage(request):
		if request.user.is_authenticated:
			return redirect('mentor')
		else:	
			if request.method == 'POST':
				username = request.POST.get('username')
				password = request.POST.get('password')

				user = authenticate(request, username=username, password=password)

				if user is not None:
					login(request, user)
					return redirect('mentor')

				else:
					messages.info(request, 'username OR password is incorrect')


			context = {}
			return render(request, 'mentor/login.html', context)



def logoutUser(request):
	logout(request)
	return redirect('login')