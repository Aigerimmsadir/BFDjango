from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField()
    due_to = models.DateTimeField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'main_tasks')
    mark = models.BooleanField();
    def __str__(self):
        return "{}: {},{},{},{}".format(self.title, self.created, self.due_to,self.owner,self.mark)
