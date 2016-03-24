'''A view is a place where we put the "logic" of our application. 
It will request information from the model you created before and pass it to a template'''


from django.shortcuts import render

# Create your views here.
#Views are just Python functions we write inside view


#we created a function (def) called post_list
#that takes request and return a function render
#this function will render (ie put together) our template named blog/post_list.html
def post_list(request):
    return render(request, 'blogapp/post_list.html', {}) #return renderd blogapp/post_list.html to the request recieved
