from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post,Comment
from django.contrib.auth.decorators import login_required
import datetime
from django.http import Http404
from django.db.models.functions import Length
from .forms import PostForm,PostUpdateForm,CommentForm

def index(request):
    posts = Post.objects.all()
    context = {'posts':posts }
    return render(request,'blog-posts.html',context)

def read_post(request,post_id):
    curpost = Post.objects.get(id = post_id)
    comments = curpost.comments.all()
    context={'curpost':curpost,'comments':comments}
    return render(request,'post.html',context)
@login_required
def add_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post = Post()
            post.title = title
            post.content = content
            post.created = datetime.datetime.now()
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request,'add_post.html',context)
@login_required
def delete_post(request,post_id):

    curpost = Post.objects.get(id=post_id)
    curpost.delete()
    return redirect('index')
@login_required
def update_post(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post.title = title
            post.content = content
            post.save()
            return redirect('index')
    else:
        form =PostUpdateForm()
    context = {'form': form,'post':post}
    return render(request,'update_post.html',context)
def add_comment(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            comment = Comment()
            comment.content=content
            comment.created = datetime.datetime.now()
            if request.user.is_authenticated:
                comment.author = request.user
            else:
            	comment.author=User.objects.get(username='guest')
            comment.post = post
            comment.save()
            return redirect('index')
    else:
        form =CommentForm()
    context = {'form': form,'post':post}
    return render(request,'add_comment.html',context)
