from main.models import Task
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from main.serializers import TaskModelSerializer,UserSerializer
@api_view(['GET'])
@csrf_exempt
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

