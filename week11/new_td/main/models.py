from django.db import models
from django.contrib.auth.models import User

class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)
class Task(models.Model):
    title =  models.CharField(max_length=80)
    created = models.DateTimeField()
    due = models.DateTimeField()
    objects = TaskManager()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    mark = models.BooleanField()
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'owner': self.owner.username if self.owner else None,
            'created': self.created,
            'due': self.due,
            'mark':self.mark
        }