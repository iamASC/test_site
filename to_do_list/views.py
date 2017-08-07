from django.db import models
from django.shortcuts import render
from to_do_list.models import Category,Task
import datetime
from django.http import HttpResponse, HttpResponseRedirect
#from to_do_list.forms import CategoryForm
from django.forms import modelformset_factory
from django.forms.widgets import SelectDateWidget
from django.views.generic import ListView
# Create your views here.

class CategoryList(ListView):
    context_object_name = 'category_list'
    template_name = 'to_do_list/index.html'
    queryset = Category.objects.annotate(num_task = models.Count('task'))\
               .order_by('-num_task')

class TaskList(ListView):
    title_dict = {
        'today': "Today's Tasks",
        'week': "Week's Tasks",
        'overdue': "Overdue Tasks",
    }
    context_object_name = 'task_list'
    template_name = 'to_do_list/task_list.html'

    def get_context_data(self, **kwargs):
        context = super(TaskList, self).get_context_data(**kwargs)
        context['title'] = self.title_dict[self.request.GET['period']]
        return context

    def get_queryset(self):
        if self.request.GET['period'] == 'today':
            return Task.objects.filter(deadline=datetime.date.today())
        elif self.request.GET['period'] == 'week':
            return Task.objects.filter(
                deadline__range=(datetime.date.today(), datetime.date.today() + datetime.timedelta(days=7)))
        elif self.request.GET['period'] == 'overdue':
            return Task.objects.filter(deadline__lt=datetime.date.today())
        else:
            return None


def category_edit(request):
    CategoryFormset = modelformset_factory(Category, fields=('name',), can_delete=True)
    if request.method == 'POST':
        formset = CategoryFormset(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/todolist/edit/category/')
    else:
        formset = CategoryFormset()
        return render(request, 'to_do_list/cat_edit.html',{'formset':formset,'title':'categories','addr':'category'})

def task_edit(request):
    TaskFormset = modelformset_factory(Task, fields=('text','category','deadline',), can_delete=True,
                                       widgets={'deadline': SelectDateWidget})
    if request.method == 'POST':
        formset = TaskFormset(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/todolist/edit/task/')
    formset = TaskFormset()
    return render(request, 'to_do_list/cat_edit.html',{'formset':formset,'title':'tasks','addr':'task'})



