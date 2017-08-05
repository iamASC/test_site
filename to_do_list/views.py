from django.db import models
from django.shortcuts import render
from to_do_list.models import Category,Task
import datetime
from django.http import HttpResponse
# Create your views here.

def index(request):
    cat_list=[]
    category_list = Task.objects.values('category').annotate(dcount=models.Count('category')).order_by('category').reverse()
    for cat in category_list:
        cat_list.append((Category.objects.get(pk=cat['category']), cat['dcount']))
    return render(request, 'to_do_list/index.html', {'list': cat_list})

title_dict ={
'todaytasks':"Today's Tasks",
'weektasks':"Week's Tasks",
'overtasks': "Overdue Tasks",
}

def task_list(request, url_arg):
    if url_arg == 'todaytasks':
        list = Task.objects.filter(deadline=datetime.date.today())
    elif url_arg == 'weektasks':
        list = Task.objects.filter(deadline__range=( datetime.date.today(), datetime.date.today() + datetime.timedelta(days = 7)))
    elif url_arg == 'overtasks':
        list = Task.objects.filter(deadline__lt= datetime.date.today())
    return render(request, 'to_do_list/task_list.html',{'title':title_dict[url_arg], 'list':list})

