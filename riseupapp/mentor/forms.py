from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# This creates a form which takes details required for user registration.
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


