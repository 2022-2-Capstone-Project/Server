import json

from django.contrib.auth.models import Permission, User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from . import models, serializers
# from .serializers import UserJWTSignUpSerializer
from .forms import SignUpForm
from .models import Profile
from .serializers import ProfileJWTSignUpSerializer
from .serializers import TokenObtainPairSerializer
from .serializers import ProfileSerializer
from tour.models import Tour
from tour_application.models import TourApplication

from point_shop.models import PointShop


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.AllowAny]


class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer


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


class JwtTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class ProfileDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, username):
        try:
            profile = models.Profile.objects.get(username=username)
            return profile
        except ObjectDoesNotExist:
            return None

    def get(self, request, username, format=None):
        post = self.get_object(username)
        serializer = serializers.ProfileSerializer(post)
        return Response(serializer.data)


class WatchPremiumTheme(APIView):
    serializer_class = serializers.ProfileSerializer

    def patch(self, request):
        user = self.request.user

        user = Profile.objects.get(username=user)

        if user.point < 100:
            return Response("not enough point")

        user.point -= 100

        serializer = ProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)

        return Response("fail")


class BuyProduct(APIView):
    serializer_class = serializers.ProfileSerializer

    def patch(self, request, product_id):
        user = self.request.user

        user = Profile.objects.get(username=user)

        product = PointShop.objects.get(id=product_id)
        print(f"price = {product.price}")

        if user.point < product.price:
            return Response("not enough point")

        user.point -= product.price

        serializer = ProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)

        return Response("fail")