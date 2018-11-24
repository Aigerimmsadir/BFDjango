from django.contrib.auth.models import User

from django.db import models
class Advert(models.Model):

    title = models.CharField(max_length=80)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    num_views = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adverts')
