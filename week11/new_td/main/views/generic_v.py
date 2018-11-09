from rest_framework import generics

from main.serializers import TaskModelSerializer,UserSerializer
from main.models import Task
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class IsSuperAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class GenericTaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    authentication_classes = (TokenAuthentication, )
   # permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Task.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class GenericTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    authentication_classes = (TokenAuthentication, )
    #permission_classes = (IsAuthenticated, )
    lookup_field = 'task_id'

    def get_object(self):
        return Task.objects.get(id=self.kwargs[self.lookup_field])

    def get_queryset(self):
        return Task.objects.for_user(self.request.user)
