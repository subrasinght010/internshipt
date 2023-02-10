from django.contrib import admin

from .models import User, Profile, Address, Patient, Doctor

# Register your models here.

admin.site.register(Doctor)

admin.site.register(Patient)

admin.site.register(Address)
admin.site.register(Profile)