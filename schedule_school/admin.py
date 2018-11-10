from django.contrib import admin
from . import models
# Register your models here.
class Schedule(admin.ModelAdmin):
	admin.site.register(models.Schedule)
	admin.site.register(models.Class_Name) 
	admin.site.register(models.Day)
	admin.site.register(models.Teacher)
	admin.site.register(models.Subject)