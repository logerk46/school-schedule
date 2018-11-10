from django.db import models
from django.utils import timezone

# Create your models here.
class Schedule(models.Model):
	id = models.AutoField(primary_key=True)
	room_number = models.IntegerField()
	id_teacher = models.IntegerField()
	id_class = models.IntegerField()
	id_subject = models.IntegerField()
	id_day = models.IntegerField()
	id_lesson_number = models.IntegerField()

class Class_Name(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=255)

	def __str__(self):
		return self.name

class Teacher(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=255)
	id_block = models.IntegerField()

	def __str__(self):
		return self.name
	
class Subject(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=255)

	def __str__(self):
		return self.name

class Day(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=255)

	def __str__(self):
		return self.name



