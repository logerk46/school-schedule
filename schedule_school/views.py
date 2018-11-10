from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models

# Create your views here.

def print_schedule(s):
    return (f"[{s.room_number}{s.id_class} {s.id_subject} "
            f"{s.id_day} {s.lesson_number}]")

def list(request):
	if('class_name' in request.GET):
		schedule_list = []
		rclass = request.GET['class_name']
		classn = models.Class_Name.objects.all().filter(name=rclass)
		classn = models.Class_Name.objects.all().filter(name=rclass)
		for day_id in range(1, 6):
			Schedule = models.Schedule.objects.all().filter(id_day=day_id, id_class=classn[0].id)
			days = {}
			days['day_id'] = day_id
			days['schedule'] = Schedule
			schedule_list.append(days)
		return HttpResponse(schedule_list)
			
		# return HttpResponse([print_schedule(s) for s in Schedule])
	else:
		return HttpResponse(f"Not enough parametrs")
