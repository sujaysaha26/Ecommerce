from django.contrib import admin

# Register your models here.
from .models import Blogpost

# We have to register here after migrating models.
admin.site.register(Blogpost)