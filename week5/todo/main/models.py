from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField()
    due_to = models.DateTimeField()
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    mark = models.BooleanField();
    def __str__(self):
        return "{}: {},{},{},{}".format(self.title, self.created, self.due_to,self.owner,self.mark)
