from rest_framework import serializers
from main.models import Task
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueValidator
import datetime


# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=300)
#     email = serializers.EmailField()
#     is_staff = serializers.BooleanField()
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', )
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class TaskModelSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    due_to =  serializers.DateTimeField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'owner','due_to','created','mark']


    def create(self, validated_data):
        task = Task(**validated_data)
        task.created=datetime.datetime.now()
        task.due = datetime.datetime.now() + datetime.timedelta(days=1, hours=3)
        task.save()
        return task
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.mark = validated_data.get('mark', instance.mark)
        instance.save()
        return instance
