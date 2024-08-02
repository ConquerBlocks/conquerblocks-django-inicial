from django.contrib import admin

from .models import Course

@admin.register(Course)
class CourseResource(admin.ModelAdmin):
    model = Course
    list_display = ("title", "created_at")
