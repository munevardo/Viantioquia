from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'backend.views.landing_views.index'),
    url(r'^jardin/$', 'backend.views.landing_views.jardin'),
    url(r'^hispania/$', 'backend.views.landing_views.hispania'),
    url(r'^andes/$', 'backend.views.landing_views.andes')
) + staticfiles_urlpatterns()
