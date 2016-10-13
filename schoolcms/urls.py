from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = [
    # Examples:
    # url(r'^$', 'schoolcms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^school/', include('school.urls')),
    url(r'^$', lambda r: HttpResponseRedirect('school/')),
]
