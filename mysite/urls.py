from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import views

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^users/',include('users.urls') ),

     


)