from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post,Author
import datetime
import datetime

def index(request):
    posts = Post.objects.all()
    context = {'posts':posts }
    return render(request,'blog-posts.html',context)