from django.contrib import admin

from .models import Organization,Employees

# Register your models here.

admin.site.register(Organization)
admin.site.register(Employees)