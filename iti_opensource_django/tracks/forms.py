from django import forms
from .models import Track, Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = "__all__"
