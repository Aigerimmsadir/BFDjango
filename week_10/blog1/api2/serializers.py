from rest_framework import serializers
from main.models import Post, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title =  serializers.CharField(max_length=100)
    created =  serializers.DateTimeField()
    author =   UserSerializer(read_only=True)
    content=  serializers.CharField(max_length=500)

    def create(self, validated_data):
        post = Post(**validated_data)
        post.author = User.objects.first()
        post.created = datetime.datetime.now()
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class PostModelSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author','created','content']
class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    post =  PostSerializer()
    created =  serializers.DateTimeField()
    author =   UserSerializer(read_only=True)
    content= serializers.CharField(max_length=500)

    def create(self, validated_data):
        comment = Comment(**validated_data)
        comment.author = User.objects.first()
        comment.created = datetime.datetime.now()
        comment.save()
        return comment


class CommentModelSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'post', 'author','created','content']