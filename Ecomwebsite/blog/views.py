from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.

def index(request):
	# To get all elements of the objects we have to use objects.all() function after that in return call it in a dictonary
    myposts = Blogpost.objects.all()
    return render(request, 'blog/index.html', {'myposts':myposts})

def blogpost(request, id):
	# After adding id in urls, we have to mention here the id so that we can easily call any function by it's id.
    post = Blogpost.objects.filter(post_id=id)[0]
    return render(request, 'blog/blogpost.html', {'post':post})
