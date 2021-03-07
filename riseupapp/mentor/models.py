from django.db import models

# This deals with taking the necessary information regarding the cyber mentors.
# This information is then populated automatically in the mentor webpage.

class Mentor(models.Model):
	name 			= models.CharField(max_length=200, null=True)
	upbringing 		= models.TextField(max_length=50, default='Location of Upbringing: ')
	certifications 	= models.CharField(max_length=200, null=True)
	expertise		= models.CharField(max_length=50, 	null='Area of Expertise: ')
	email 			= models.EmailField(max_length=200, null=True)
	available		= models.TextField(max_length=50, default='Yes')
	

	def __str__(self):
		return self.name
