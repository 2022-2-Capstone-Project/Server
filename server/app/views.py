from django.contrib.auth.models import User, Permission
from rest_framework import viewsets, permissions

from app import serializers, models


class TourThemeViewSet(viewsets.ModelViewSet):
    queryset = models.TourTheme.objects.all().order_by('-created')
    serializer_class = serializers.TourThemeSerializer
    permission_classes = [permissions.AllowAny]


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
