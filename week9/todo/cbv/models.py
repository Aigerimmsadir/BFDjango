from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

class Task(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField()
    due_to = models.DateTimeField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'cbv_tasks')
    objects = TaskManager()
    mark = models.BooleanField();
    def __str__(self):
        return "{}: {},{},{},{}".format(self.title, self.created, self.due_to,self.owner,self.mark)

    def get_absolute_url(self):
        return reverse_lazy('cbv:index')