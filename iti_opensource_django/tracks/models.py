from django.db import models


# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

    def is_graduated(self):
        return self.age > 20

    is_graduated.boolean = True
    track.short_description = "Graduated"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
