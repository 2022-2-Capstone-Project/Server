from django.contrib.auth.models import User, Permission
from rest_framework import serializers

from .models import TourTheme, Profile


class TourThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TourTheme
        fields = '__all__'


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
