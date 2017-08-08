from django.conf.urls import url
from to_do_list import views

urlpatterns = [
    url(r'^$', views.CategoryList.as_view(), name='index'),
    url(r'^tasklist/$', views.TaskList.as_view(), name='tasklist'),
    url(r'^edit/(category)/$', views.Editor.as_view(), name='category_edit'),
    url(r'^edit/(task)/$', views.Editor.as_view(), name='task_edit'),
    url(r'^edit/task/update/$', views.AjaxUpdater.as_view(), name='task_edit'),
]