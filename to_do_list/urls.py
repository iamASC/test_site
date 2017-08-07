from django.conf.urls import url
from to_do_list import views

urlpatterns = [
    url(r'^$', views.CategoryList.as_view(), name = 'index'),
    url(r'^tasklist/$', views.TaskList.as_view(), name = 'tasklist'),
    url(r'^edit/category/$', views.category_edit, name = 'category_edit'),
    url(r'^edit/task/$', views.task_edit, name = 'task_edit'),

]