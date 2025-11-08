from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer, LoginSerializer

class UserViewSet(viewsets.ModelViewSet):
  querySet = User.objects.all()
  serializer_class = UserSerializer

  def get_permissions(self):
    if self.action == 'login':
      return [AllowAny()]
    return [IsAuthenticated()]

  def create(self, request, *args, **kwargs):
    if request.user.role != 'ADMIN':
      return Response(
        {'error': 'Only admins can create users'},
        status=status.HTTP_403_FORBIDDEN
      )
    return super().create(request, *args, **kwargs)

  def update(self, request, *args, **kwargs):
    if request.user.role != 'ADMIN':
      return Response(
        {'error': 'Only admins can update users'},
        status=status.HTTP_403_FORBIDDEN
      )
    return super().update(request, *args, **kwargs)

  def destroy(self, request, *args, **kwargs):
    if request.user.role != 'ADMIN':
      return Response(
        {'error': 'Only admins can delete users'},
        status=status.HTTP_403_FORBIDDEN
      )
    return super().destroy(request, *args, **kwargs)

  @action(detail=False, methods=['post'], permission_classes=[AllowAny])
  def login(self, request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(
      username=serializer.validated_data['username'],
      password=serializer.validated_data['password']
    )

    if user is None:
      return Response(
        {'error': 'Invalid Credentials'},
        status=status.HTTP_401_UNAUTHORIZED
      )

    if user.role != 'ADMIN':
      return Response(
        {'error': 'Only admins can access this system'},
        status=status.HTTP_403_FORBIDDEN
      )

    refresh = RefreshToken.for_user(user)

    return Response({
      'user': UserSerializer(user).data,
      'access': str(refresh.access_token),
      'refresh': str(refresh),
    })

  @action(detail=False, methods=['get'])
  def get_self_details(self, request):
    serializer = self.get_seralizer(request.user)
    return Response(serializer.data)
