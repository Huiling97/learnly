from rest_framework import serializers
from .models import Course, Lesson

class LessonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lesson
    fields = ['id', 'title', 'content', 'order', 'video_url']

class CourseSerializer(serializers.ModelSerializer):
  lessons = LessonSerializer(many=True, read_only=True)
  instructor_name = serializers.CharField(source='instructor.username', read_only=True)

  class Meta:
    model = Course
    fields = ['id', 'title', 'description', 'instructor', 'instructor_name', 'lessons', 'created_at', 'updated_at', 'is_published']
    read_only_fields = ['created_at', 'updated_at']
