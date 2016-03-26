from django.conf.urls import include, url
from django.conf.urls import url
from . import views

#if theris some text inside ^$ inside the url  then empty  url request from user 
#wont give the view_named post_list
#post_list is viewed when the user requests contains empty string ie nothing after 127.0.0.1:8000/'nothing here'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about.html$', views.about, name='about'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^subdivisions.html$', views.subdiv, name='subdivisions'),
    url(r'^contact.html$', views.contact, name='contact'),
    url(r'^blog.html$', views.blog, name='blog'),    
]


