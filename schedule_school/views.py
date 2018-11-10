from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . import models

# Create your views here.

def print_schedule(s):
    return (f"[{s.room_number} {s.id_teacher} {s.id_class} {s.id_subject} "
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
        return render(request, 'schedule_school/index.html', {'schedule': schedule_list})
            
        # return HttpResponse([print_schedule(s) for s in Schedule])
    else:
        return HttpResponse(f"Not enough parametrs")


@csrf_exempt
def add(request):

    if request.method == 'POST':
        fields = ('room_number', 'id_teacher', 'id_class', 'id_subject',
                  'id_day', 'lesson_number')
        fields = (room_number, id_teacher, id_class, id_subject, id_day,
                  lesson_number) = [request.GET.get(v) for v in fields]
        if not all(fields):
            return HttpResponse(f"Not enough parametrs")
        else:
            teacher = models.Teacher.objects.filter(name=id_teacher)
            id_class = models.Class_Name.objects.filter(name=id_class)
            id_subject = models.Subject.objects.filter(name=id_subject)
            id_day = models.Day.objects.filter(name=id_day)
            s = models.Schedule(room_number=room_number,
                                id_teacher=teacher,
                                id_class=id_class,
                                id_subject=id_subject,
                                id_day=id_day,
                                lesson_number=lesson_number)
            s.save()
            return HttpResponse("ok")
