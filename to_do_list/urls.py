from django.conf.urls import url
from to_do_list import views

urlpatterns = [
    url(r'^todaytasks/$', views.todaytasks, name = 'todaytasks'),
    url(r'^weektasks/$', views.weektasks, name = 'weektasks'),
    url(r'^overtasks/$', views.overtasks, name = 'overtasks'),

]