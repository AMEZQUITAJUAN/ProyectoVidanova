from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    nid = models.CharField(max_length=20)

