from django.db import models

# Create your models here.

class Mentor(models.Model):
	name 			= models.CharField(max_length=200, null=True)
	upbringing 		= models.TextField(max_length=50, default='Location of Upbringing: ')
	certifications 	= models.CharField(max_length=200, null=True)
	expertise		= models.CharField(max_length=50, 	null='Area of Expertise: ')
	email 			= models.EmailField(max_length=200, null=True)
	available		= models.TextField(max_length=50, default='Yes')
	

	def __str__(self):
		return self.name