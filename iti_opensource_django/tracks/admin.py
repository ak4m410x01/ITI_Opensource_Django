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

    list_display = (
        "first_name",
        "last_name",
        "age",
        "track",
    )


class InlineStudent(admin.StackedInline):
    model = Student
    extra = 1


class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent]


# Register your models here.

admin.site.register(Track, CustomTrack)
admin.site.register(Student, CustomStudent)
