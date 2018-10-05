from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Task,Owner
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all();
    context = {'tasks':tasks }
    return render(request,'todo_list.html',{'tasks':tasks })

def completed_tasks(request):
    tasks =  Task.objects.filter(mark=True);
    context = {'tasks':tasks }
    return render(request,'completed_todo.html',context)

def incompleted_tasks(request):
    tasks =  Task.objects.filter(mark=False);
    context = {'tasks':tasks }
    return render(request,'completed_todo.html',context)

def creation_order(request):
    tasks =  Task.objects.all().order_by("created");
    context = {'tasks':tasks }
    return render(request,'completed_todo.html',context)
def due_order(request):
    tasks =  Task.objects.all().order_by("due_to");
    context = {'tasks':tasks }
    return render(request,'completed_todo.html',context)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request,'newtask.html',context)
def delete_task(request, task_id):
    try:
        curtask = Task.objects.get(id=task_id)
        curtask.delete()
    except Task.DoesNotExist:
        raise Http404("Task not found")
    return redirect('index')
def delete_list(request):
    Task.objects.all().delete()
    return redirect('index')

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
    