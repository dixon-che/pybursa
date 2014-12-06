from django.conf.urls import patterns, include, url
from courses.views import courses_list, courses_item


urlpatterns = patterns(
    '',
    url(r'^$', courses_list, name="index"),
    url(r'^(?P<course_id>\d+)/$', courses_item, name="detail"),
)
