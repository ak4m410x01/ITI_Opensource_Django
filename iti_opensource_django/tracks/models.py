from django.db import models


# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=200)


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
