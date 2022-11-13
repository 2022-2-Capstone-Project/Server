from django.contrib.auth.models import User, Permission
from rest_framework import serializers
from .models import Profile


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


class UserJWTSignUpSerializer(serializers.ModelSerializer):

    email = serializers.CharField(
        required=True,
        # write_only=True,
        max_length=20
    )

    password = serializers.CharField(
        required=True,
        # write_only=True,
        style={'input_type': 'password'}
    )

    username = serializers.CharField(
        required=True,
        # write_only=True,
        max_length=20
    )

    class Meta:
        model = User
        fields = ['email', 'password', 'username']

    def save(self, **kwargs):
        user = super().save()

        user.email = self.validated_data['email']
        user.set_password(self.validated_data['password'])
        user.username = self.validated_data['username']
        user.save()

        return user

    def validate(self, data):
        email = data.get('email', None)

        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError("User already exists")

        return data