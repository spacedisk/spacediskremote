"""site_src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [

    #the user ur request if contins admin will be passed  into  the admin
    url(r'^admin/', admin.site.urls),
    #the url reqquest from user if empty will be passed into the urls.py file under blogapp folder
    #ie /blogapp/url.py
    url(r'', include('blogapp.urls')),
    url(r'about.html', include('blogapp.urls')),
    url(r'index.html', include('blogapp.urls')),
    url(r'subdivisions.html', include('blogapp.urls')),
    url(r'contact.html', include('blogapp.urls')),
    url(r'blog.html', include('blogapp.urls')),
    url(r'realdat.html', include('blogapp.urls')),
       
]
