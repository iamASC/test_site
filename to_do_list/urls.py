from django.conf.urls import url
from to_do_list import views

urlpatterns = [
    url(r'^(todaytasks)/$', views.task_list, name = 'todaytasks'),
    url(r'^(weektasks)/$', views.task_list, name = 'weektasks'),
    url(r'^(overtasks)/$', views.task_list, name = 'overtasks'),

]