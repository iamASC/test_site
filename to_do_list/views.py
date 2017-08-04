from django.shortcuts import render
from to_do_list.models import Category,Task
import datetime
from django.http import HttpResponse
# Create your views here.

def todaytasks(request):
    today = Task.objects.filter(deadline=datetime.date.today())
    res = ''
    for task in today:
        res += task.category.name + ":" + task.text + ":" + str(task.deadline) +"<br>"
    return HttpResponse(res)


def weektasks(request):
    week = Task.objects.filter(deadline__range=(datetime.date.today(), datetime.datetime.today() + datetime.timedelta(days = 7)))
    res = ''
    for task in week:
        res += task.category.name + ":" + task.text + ":" + str(task.deadline) + "<br>"
    return HttpResponse(res)

def overtasks(request):
    over = Task.objects.filter(deadline__lt= datetime.datetime.today())
    res = ''
    for task in over:
        res += task.category.name + ":" + task.text + ":" + str(task.deadline) + "<br>"
    return HttpResponse(res)

