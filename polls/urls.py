#from django.conf.urls import patterns, url

from django.conf.urls import *
from django.conf import settings
import django.views.static


from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

    #url(r'^login/$',views.login,),
    #url(r'^login/test/$', views.index, name='index'),
    #(r'^emailverif/', include('emailverification.urls')),
    #(r'^registration/', include('registration.backends.default.urls')),
    #(r'^accounts/login/?$', 'registration.views.loginform'), # Django adds a slash when logging out?
    #(r'^accounts/logout$', 'django.contrib.auth.views.logout', { "redirect_field_name": "next" }),
    #(r'^accounts/profile$', 'registration.views.profile'),
   
    #{'template_name':'registration/login.html'} ),
)