from django.contrib.auth.models import User, Permission
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

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

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, **kwargs):
        user = super().save()

        user.username = self.validated_data['username']
        user.set_password(self.validated_data['password'])
        user.save()

        return user

    def validate(self, data):
        username = data.get('username', None)

        if User.objects.filter(username = username).exists():
            raise serializers.ValidationError("username already exists")

        return data


# class UserJWTSignInSerializer(serializers.ModelSerializer):
#
#     username = serializers.CharField(
#         required=True,
#         # write_only=True,
#         max_length=20
#     )
#
#     password = serializers.CharField(
#         required=True,
#         # write_only=True,
#         style={'input_type': 'password'}
#     )
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#
#     def validate(self, data):
#         username = data.get('username', None)
#         password = data.get('password', None)
#
#         if User.objects.filter(username=username).exists():
#             user = User.objects.get(username=username)
#
#             if not user.check_password(password):
#                 raise serializers.ValidationError("비밀번호가 틀렸습니다.")
#         else:
#             raise serializers.ValidationError("유저가 존재하지 않습니다.")
#
#         return data