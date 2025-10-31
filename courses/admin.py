from django.contrib import admin
from .models import Course, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
  list_display = ['title', 'instructor', 'is_published', 'created_at']
  list_filter = ['is_published', 'created_at']
  search_fields = ['title', 'description']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
  list_display = ['title', 'course', 'order']
  list_filter = ['course']
