from django.contrib import admin
from .models import Track, Student


class CustomStudent(admin.ModelAdmin):
    fieldsets = (
        [
            "Student Information",
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "age",
                ],
            },
        ],
        [
            "Scholarship Information",
            {
                "fields": [
                    "track",
                ],
            },
        ],
    )


# Register your models here.

admin.site.register(Track)
admin.site.register(Student, CustomStudent)
