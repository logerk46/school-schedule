from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models

# Create your views here.

def print_schedule(s):
    return (f"[{s.room_number} {s.id_teacher} {s.id_class} {s.id_subject} "
            f"{s.id_day} {s.lesson_number}]")

def list(request):

	if('day' in request.GET and 'class_name' in request.GET):
		rday = request.GET['day']
		rclass = request.GET['class_name']
		classn = models.Class_Name.objects.all().filter(name=rclass)
		Schedule = models.Schedule.objects.all().filter(id_day=rday)
		return HttpResponse([print_schedule(s) for s in Schedule])
	else:
		return HttpResponse(f"Not enough parametrs")
