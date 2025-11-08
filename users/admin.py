from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
  list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_active']
  list_filter = ['role', 'is_active']
  search_fields = ['username', 'email', 'first_name', 'last_name', 'student_id', 'employee_id']
  
  # Fields displayed when editing user
  fieldsets = UserAdmin.fieldsets + (
    ('Additional Info', {
      'fields': ('phone_number', 'date_of_birth')
    }),
    ('Student Info', {
      'fields': ('enrollment_year', 'major'),
      'classes': ('collapse',)
    }),
    ('Lecturer Info', {
      'fields': ('department', 'specialization'),
      'classes': ('collapse',)
    }),
    ('Status', {
      'fields': ('is_verified',)
    })
  )

  # Fields displayed when adding new user
  add_fieldsets = UserAdmin.add_fieldsets + (
    (None, {
      'fields': ('first_name', 'last_name', 'role', 'email', 'phone_number', 'date_of_birth' )
    }),
  )