
from django.conf.urls import patterns, include, url

from models import Post
import views

urlpatterns = patterns('',
    url(r'^post/(?P<slug>[-\w]+)$', 
        'users.views.view_post',
        name='blog_post_detail'),
    url(r'^add/post$', 
        'users.views.add_post', 
        name='blog_add_post'),
    url(r'^viewall$', 
        'users.views.viewall', 
        name='viewall'),
    url(r'^blog/(\w+)/$', 
     'users.views.blog', 
       name='blog'),
     url(r'^(\w+)/$', 'users.views.myview', name='myview'),
      url(r'^(\w+)/(\w+)/$', 'users.views.showpost', name='showpost'),
    
)