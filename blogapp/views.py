'''A view is a place where we put the "logic" of our application. 
It will request information from the model you created before and pass it to a template'''


from django.shortcuts import render
from .models import Post #this is to import the  object post of class models 
from django.utils import timezone #so we can query using timezone of published posts
#now we could use quieries to filter order and view instance of this object which are 
#originally posts published in the databse 
""" published posts inherits Post class and Post class inherits from models class
thus posts are objects of Post and Post is an object of models in django DRM"""


# Create your views here.
#Views are just Python functions we write inside view


#we created a function (def) called post_list
#that takes request and return a function render
#this function will render (ie put together) our template named blog/post_list.html
def post_list(request):
    #return render(request, 'blogapp/post_list.html', {}) #return renderd blogapp/post_list.html to the request recieved
    #we created  posts as  variable or instance of class Post in models  
    #accessing ths function post.objects.filter()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #so request is everything we receive from the user via the Internet + template file 'blog/post_list.html'
    #{'posts': posts} is some things for the template to use while request is renederd vi
    return render(request, 'blogapp/post_list.html', {'posts': posts})