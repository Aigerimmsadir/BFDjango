from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Task
from api2.serializers import TaskSerializer, TaskModelSerializer
import json


@csrf_exempt
def tasks_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskModelSerializer(data=data)
        if serializer.is_valid():
            print ("vaalid!")
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': 'invalid data'})


@csrf_exempt
def tasks_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        serializer = TaskModelSerializer(task)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TaskModelSerializer(instance=task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': 'invalid data'})
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'deleted': True})


