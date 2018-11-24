from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from main.serializers import AdvertModelSerializer,UserSerializer
from main.models import Advert

class AdvertList(APIView):
    def get(self,request):
        adverts = Advert.objects.filter(owner = request.user)
        serializer = AdvertModelSerializer(adverts,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AdvertModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(owner = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvertDetail(APIView):
    def get_object(self,pk):
        advert = Advert.objects.get(id = pk)
        return advert
    def get(self,pk):
        advert = self.get_object(pk)
        serializer = AdvertModelSerializer(advert)
        advert.num_views+=1
        advert.save()
        return Response(serializer.data)

    def put(self, request, pk):
        advert = self.get_object(pk)
        serializer = AdvertModelSerializer(instance=advert, data=request.data)
        if serializer.is_valid():
            serializer.save(owner =self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        advert = self.get_object(pk)
        advert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
