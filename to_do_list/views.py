import datetime
from django.db import models
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory,DateInput
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from to_do_list.models import Category,Task


class CategoryList(ListView):
    context_object_name = 'category_list'
    template_name = 'to_do_list/index.html'
    queryset = Category.objects.annotate(num_task = models.Count('task'))
    queryset = queryset.order_by('-num_task')


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
            return Task.objects.filter(deadline__range=(
                                            datetime.date.today(),
                                            datetime.date.today() + datetime.timedelta(days=7)
                                            ))
        elif self.request.GET['period'] == 'overdue':
            return Task.objects.filter(deadline__lt=datetime.date.today())
        else:
            return None

CategoryFormset = modelformset_factory(Category, fields=('name',),
                                       can_delete=True)
TaskFormset = modelformset_factory(Task,
                                   fields=('text', 'category', 'deadline','is_complete'),
                                   can_delete=True,
                                   widgets={
                                       'deadline':DateInput(attrs={'class':'datepicker'})
                                   }
                                   )
class Editor(TemplateView):
    template_name = 'to_do_list/category_edit.html'
    formset = None

    def get(self, request, *args, **kwargs):
        if args[0] == 'category':
            self.formset = CategoryFormset()
        elif args[0] == 'task':
            self.formset = TaskFormset()
        return super(Editor, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Editor, self).get_context_data(**kwargs)
        context['formset'] = self.formset
        if self.args[0] == 'category':
            context['title'] = 'categories'
            context['addr'] = 'category'
        elif self.args[0] == 'task':
            context['title'] = 'tasks'
            context['addr'] = 'task'
        return context

    def post(self, request, *args, **kwargs):
        if args[0] == 'category':
            self.formset = CategoryFormset(request.POST)
        elif args[0] == 'task':
            self.formset = TaskFormset(request.POST)
        if self.formset.is_valid():
            self.formset.save()
            if args[0] == 'category':
                return HttpResponseRedirect('/todolist/edit/category/')
            elif args[0] == 'task':
                return HttpResponseRedirect('/todolist/edit/task/')
        return super(Editor,self).get(self, request, *args, **kwargs)
