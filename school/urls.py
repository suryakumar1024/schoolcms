from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^class/(?P<cls>[0-9]+)$', views.get_class_details, name='details'),
    url(r'^staff/(?P<stf>[0-9]+)$', views.get_staff_details, name='staff'),
    url(r'^class/(?P<cls>[0-9]+)/add_std/$', views.add_student, name='add_student'),
    url(r'^class/(?P<std>[0-9]+)/add_mark/$', views.addmark, name='addmark'),
    url(r'^class/(?P<std>[0-9]+)/delete_student/$', views.delete, name='delete'),
    url(r'^class/(?P<cls>[0-9]+)/(?P<subject>[\w\-]+)/ranking/$', views.get_class_details, name='subject_sort'),
    url(r'^staff/add_grp/(?P<cls>[0-9]+)/$', views.student_generator, name='generator'),
]
