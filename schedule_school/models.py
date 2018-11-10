from django.db import models
from django.utils import timezone

# Create your models here.
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


class Schedule(models.Model):
	id = models.AutoField(primary_key=True)
	room_number = models.IntegerField()
	id_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	id_class = models.ForeignKey(Class_Name, on_delete=models.CASCADE)
	id_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	id_day = models.ForeignKey(Day, on_delete=models.CASCADE)
	lesson_number = models.IntegerField()
