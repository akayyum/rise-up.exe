from django import forms 

from .models import mentors

class mentorform(forms.ModelForm):
	class Meta:
		model = mentors
		fields = [
			'title',
			'upbringing',
			'expertise'

		]