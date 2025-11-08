from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  ROLE_CHOICES = [
    ('STUDENT', 'Student'),
    ('LECTURER', 'Lecturer'),
    ('ADMIN', 'Admin')
  ]

  role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='STUDENT')
  phone_number = models.CharField(max_length=15, blank=True)
  date_of_birth = models.DateField(null=True, blank=True)
  
  # Student fields
  student_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
  enrollment_year = models.IntegerField(null=True, blank=True)
  major = models.CharField(max_length=100)

  # Lecturer fields
  employee_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
  department = models.CharField(max_length=100)
  specialization = models.CharField(max_length=100, null=True, blank=True)

  is_verified = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def get_full_name(self):
    return f"{self.first_name} {self.last_name}"

  def __str__(self):
    return f"{self.get_full_name()} ({self.role})"
