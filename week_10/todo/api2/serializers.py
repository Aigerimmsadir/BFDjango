from rest_framework import serializers
from main.models import Task
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email', )


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    owner = UserSerializer(read_only=True)
    created = serializers.DateTimeField()
    due_to =  serializers.DateTimeField()
    mark=serializers.BooleanField(required=True)
    def create(self, validated_data):
        task = Task(**validated_data)
        task.owner = User.objects.first()
        task.due_to=datetime.datetime.now() + datetime.timedelta(days=1, hours=3)
        task.created = datetime.datetime.now()
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.due_to = validated_data.get('due_to', instance.due_to)
        instance.mark = validated_data.get('mark', instance.mark)
        instance.save()
        return instance


class TaskModelSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'owner','due_to','created','mark']
