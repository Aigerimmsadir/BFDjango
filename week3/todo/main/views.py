from django.shortcuts import render
from django.http import HttpResponse
import datetime



def index(request):
    tasks = [{
            'created':"17.09.18",
            'dueto':"25.09.18",
            'owner':"me",'mark' :True},
            {'created':"17.09.18",
            'dueto':"25.09.18",
            'owner':"me",
            'mark' : True}
    ]
    context = {'tasks':tasks }
    return render(request,'todo_list_logic.html',{'tasks':tasks })

def completed_tasks(request):
	tasks = [{
	        'created':"17.09.18",
	        'dueto':"27.09.18",
	        'owner':"me",'mark' :False}
            	]
	context = {'tasks':tasks }
	return render(request,'completed_todo.html',context)

