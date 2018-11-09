from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import datetime
from main.models import Task
@csrf_exempt
def task_list_jsn(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks = [t.to_json() for t in tasks]
        return JsonResponse(tasks, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        task= Task(title=data['title'], owner=request.user,created = datetime.datetime.now()
                   ,due = datetime.datetime.now() + datetime.timedelta(days=1, hours=3), mark = False)
        task.save()
    return JsonResponse(task.to_json())
@csrf_exempt
def task_read(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        return JsonResponse(task.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        task.title = data.get('title', task.title)
        task.save()
        return JsonResponse(task.to_json())
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'deleted': True}, status=204)
@csrf_exempt
def task_completed(request):
    tasks = Task.objects.filter(mark=True)
    tasks=[t.to_json() for t in tasks]
    return JsonResponse(tasks, safe=False)
