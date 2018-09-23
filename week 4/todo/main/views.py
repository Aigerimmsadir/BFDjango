from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Task,Owner


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
def tasks_due(request):
    tasks =  Task.objects.filter(due_to =  datetime.datetime.today());
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
