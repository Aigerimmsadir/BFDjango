from rest_framework import serializers
from .models import Advert
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
import datetime

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
class AdvertModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=80),
    address = serializers.CharField(max_length=100),
    description = serializers.CharField(max_length=500),
    price = serializers.IntegerField()
    num_views = serializers.IntegerField(read_only=True)
    owner = UserSerializer(read_only=True)
    def create(self, validated_data):
        advert = Advert(**validated_data)
        advert.num_views=0
        advert.save()
        return advert
    def update(self, instance, validated_data):
        instance = AdvertModelSerializer()
        instance.title = validated_data.get('title',instance.title)
        instance.address = validated_data.get('address',instance.address)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
    class Meta:
        model = Advert
        fields = ('id', 'title', 'address', 'description', 'price', 'num_views', 'owner')