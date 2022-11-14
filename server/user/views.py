from django.contrib.auth.models import Permission, User
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from . import models, serializers
from .serializers import UserJWTSignUpSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]


class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer


class JWTSignUpView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserJWTSignUpSerializer(queryset)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserJWTSignUpSerializer(data=request.data)

        if serializer.is_valid(raise_exception=False):
            user = serializer.save(request)

            token = RefreshToken.for_user(user)
            refresh = str(token)
            access = str(token.access_token)

            return Response({
                'user': user,
                'access': access,
                'refresh': refresh,
            }, status=200)

        return Response(status=400)