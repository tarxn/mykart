from django.shortcuts import render
from .models import Blogpost
# Create your views here.
from django.http import HttpResponse

def index(request):
    post = Blogpost.objects.all()
    params= {'post' :  post}

    return render(request,'blog/index.html',params)

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id=id)[0]
    params = {'post': post}

    return render(request, 'blog/blogpost.html', params)


