from django.urls import path
from . import views

app_name = "tracks"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("student/all", views.getAllStudents, name="getAllStudents"),
    path("student/<int:id>", views.getStudent, name="getStudent"),
]
