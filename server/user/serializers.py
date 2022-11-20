from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class ProfileJWTSignUpSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        required=True,
        # write_only=True,
        max_length=20
    )

    password = serializers.CharField(
        required=True,
        # write_only=True,
        style={'input_type': 'password'}
    )

    nickname = serializers.CharField(
        required=True,
        max_length=20
    )

    user_type = serializers.CharField(
        required=True,
        max_length=10
    )

    class Meta:
        model = Profile
        fields = ['username', 'password', 'nickname', 'user_type']

    def save(self, **kwargs):
        profile = super().save()

        profile.username = self.validated_data['username']
        profile.set_password(self.validated_data['password'])
        profile.nickname = self.validated_data['nickname']
        profile.user_type = self.validated_data['user_type']
        profile.save()

        return profile

    def validate(self, data):
        username = data.get('username', None)

        if Profile.objects.filter(username = username).exists():
            raise serializers.ValidationError("username already exists")

        return data