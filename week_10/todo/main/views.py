from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Task
from django.contrib.auth.models import User
from .forms import TaskForm,TaskUpdateForm
def home(request):
    if (request.user.is_authenticated):
        return redirect('index')
    else:
        return render(request, 'home.html')
@login_required
def index(request):
    tasks = Task.objects.all();
    context = {'tasks':tasks }
    return render(request,'todo_list.html',{'tasks':tasks })
@login_required
def completed_tasks(request):
    tasks =  Task.objects.filter(mark=True);
    context = {'tasks':tasks }
    return render(request,'todo_list.html',{'tasks':tasks })
@login_required
def incompleted_tasks(request):
    tasks =  Task.objects.filter(mark=False);
    context = {'tasks':tasks }
    return render(request,'todo_list.html',{'tasks':tasks })
@login_required
def creation_order(request):
    tasks =  Task.objects.all().order_by("created");
    context = {'tasks':tasks }
    return render(request,'todo_list.html',{'tasks':tasks })
@login_required
def due_order(request):
    tasks =  Task.objects.all().order_by("due_to");
    context = {'tasks':tasks }
    return render(request,'todo_list.html',{'tasks':tasks })
@login_required
def add_task(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():

            title = form.cleaned_data['title']
            mark = form.cleaned_data['mark']
            due_to=form.cleaned_data['due_to']
            task = Task()
            task.title = title
            task.mark = mark
            task.due_to = due_to
            task.created = datetime.datetime.now()
            task.owner = request.user
            task.save()
            return redirect('index')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request,'newtask.html',context)
@login_required
def delete_task(request, task_id):
    try:
        curtask = Task.objects.get(id=task_id)
        curtask.delete()
    except Task.DoesNotExist:
        raise Http404("Task not found")
    return redirect('index')
@login_required
def delete_list(request):
    Task.objects.all().delete()
    return redirect('index')
@login_required
def task_done(request, task_id):
    try:
        curtask = Task.objects.get(id=task_id)
        if curtask.mark==False:
            curtask.mark=True
            curtask.save()
    except Task.DoesNotExist:
        raise Http404("Task not found")
    if curtask.mark==True:
        return redirect('index')
@login_required
def update_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        if request.method == 'POST':
            form = TaskUpdateForm(request.POST or None)
            
            if form.is_valid():
                title = form.cleaned_data['title']
               
                due_to = form.cleaned_data['due_to']
                
                mark=form.cleaned_data['mark']
                task.title = title 
                
                task.due_to = due_to
                
                task.mark=mark
                task.save()
                return redirect('index')
            else:
            	return HttpResponse(form.errors )
        else:
            form = TaskUpdateForm(initial={'due_to': task.due_to, 'title': task.title,'mark': task.mark})
            context = {'form': form, 'task':task}
            return render(request,'update_task.html',context)
    except Task.DoesNotExist:
         return HttpResponse("not")