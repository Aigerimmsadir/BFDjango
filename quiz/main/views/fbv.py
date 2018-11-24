from main.models import Advert
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from main.serializers import AdvertModelSerializer,UserSerializer
@api_view(['GET'])
@csrf_exempt
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def advert_list(request, format=None):
    if request.method == 'GET':
        adverts = Advert.objects.all()
        serializer = AdvertModelSerializer(adverts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdvertModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def advert_detail(request, pk):
    try:
        advert = Advert.objects.get(id=pk)
    except Advert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdvertModelSerializer(advert)
        advert.num_views=advert.num_views+1
        advert.save()
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AdvertModelSerializer(instance=advert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        advert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
