from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^admin/', include(admin.site.urls)),
)
