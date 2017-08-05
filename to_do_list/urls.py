from django.conf.urls import url
from to_do_list import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(todaytasks)/$', views.task_list, name = 'todaytasks'),
    url(r'^(weektasks)/$', views.task_list, name = 'weektasks'),
    url(r'^(overtasks)/$', views.task_list, name = 'overtasks'),
    url(r'^edit/category/$', views.category_edit, name = 'category_edit'),
    url(r'^edit/task/$', views.task_edit, name = 'task_edit'),

]