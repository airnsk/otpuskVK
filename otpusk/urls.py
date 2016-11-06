from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'main.views.home', name='home'),
                       url(r'^ajax/$', 'main.views.calculation'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
