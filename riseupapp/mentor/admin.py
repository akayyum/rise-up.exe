from django.contrib import admin

# This registers the models and initialises data for the database backend.
from .models import *

admin.site.register(Mentor)