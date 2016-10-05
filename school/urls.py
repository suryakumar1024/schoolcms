from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^class/(?P<cls>[0-9]+)$', views.get_class_details, name='details'),
    url(r'^class/(?P<cls>[0-9]+)/add_std/$', views.add_student, name='add_student'),
    url(r'^class/(?P<std>[0-9]+)/add_mark/$', views.addmark, name='addmark'),
]