from django.contrib import admin

# Register your models here.
from to_do_list.models import Category,Task
admin.site.register(Category)
admin.site.register(Task)