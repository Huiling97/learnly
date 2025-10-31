from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer

class CourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

  def get_queryset(self):
    # Only show published courses to non-staff users
    queryset = Course.objects.all()
    if not self.request.user.is_staff:
      queryset = queryset.filter(is_published=True)
    return queryset

    @action(detail=True, methods=['get'])
    def lessons(self, request, pk=None):
      course = self.get_object()
      lessons = course.lessons.all()
      serializer = LessonSerializer(lessons, many=True)
      return Response(serializer.data)
