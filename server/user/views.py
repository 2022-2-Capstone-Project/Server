from django.contrib.auth.models import Permission, User
from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from . import models, serializers
# from .serializers import UserJWTSignUpSerializer
from .forms import SignUpForm
from .serializers import ProfileJWTSignUpSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer
#     permission_classes = [permissions.AllowAny]
#     # permission_classes = [permissions.IsAuthenticated]


class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer


# class JWTSignUpView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserJWTSignUpSerializer
#
#     def create(self, request):
#         serializer = UserJWTSignUpSerializer(data=request.data)
#
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.save()
#
#             # token = RefreshToken.for_user(user)
#             # refresh = str(token)
#             # access = str(token.access_token)
#
#             return JsonResponse({
#                 'user': serializer.data,
#                 # 'access': access,
#                 # 'refresh': refresh,
#             }, status=200)
#
#         return Response(status=400)

class JWTProfileSignUpView(viewsets.ModelViewSet):
    form_class = SignUpForm
    queryset = models.Profile.objects.all()
    serializer_class = ProfileJWTSignUpSerializer

    def create(self, request):
        serializer = ProfileJWTSignUpSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            profile = serializer.save()

            # token = RefreshToken.for_user(user)
            # refresh = str(token)
            # access = str(token.access_token)

            return JsonResponse({
                'profile': serializer.data,
                # 'access': access,
                # 'refresh': refresh,
            }, status=200)

        return Response(status=400)

# class JWTSignInView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserJWTSignInSerializer
#
#     # def list(self, request):
#     #     serializer = UserJWTSignInSerializer(data=request.data)
#     #
#     #     if serializer.is_valid(raise_exception=True):
#     #         return Response(serializer.data, status=200)
#     #
#     #     return Response(status=400)
#
#     def create(self, request, *args, **kwargs):
#         serializer = UserJWTSignInSerializer(data=request.data, many=True)
#
#         if serializer.is_valid(raise_exception=True):
#
#             token = RefreshToken.for_user(serializer[0].data)
#             refresh = str(token)
#             access = str(token.access_token)
#
#             return JsonResponse({
#                 'user': serializer.data,
#                 'access': access,
#                 'refresh': refresh,
#             }, status=200)
#
#         return Response(status=400)


