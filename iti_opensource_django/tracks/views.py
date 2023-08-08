from django.shortcuts import render
from django.http import HttpResponse
from .models import Track, Student


# Create your views here.


def home(request):
    return HttpResponse("<h1>Home Page...</h1>")


def getAllStudents(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, "tracks/students.html", context)


def getStudent(request, id: int):
    student = Student.objects.get(id=id)
    context = {"student": student}
    return render(request, "tracks/student.html", context)
