from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True, required=False)

  class Meta:
    model = User
    fields = [
      'id', 'username', 'email', 'first_name', 'last_name', 
      'role', 'phone_number', 'date_of_birth','student_id', 'enrollment_year', 'major',
      'employee_id', 'department', 'specialization',
      'is_active', 'is_verified', 'created_at', 'updated_at',
      'password'
    ]
    read_only_fields = ['id', 'student_id', 'employee_id', 'created_at', 'updated_at']

    def create(self, validated_data):
      password = validated_data.pop('password', None)
      user = User(**validated_data)
      if password:
        user.set_password(password)
      user.save()
      return user

    def update(self, instance, validated_data):
      password = validated_data.pop('password', None)
      for attr, value in validated_data.items():
        setattr(instance, attr, value)
      if password:
        instance.set_password(password)
      instance.save()
      return instance

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField(write_only=True)
