from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from .models import PointShop
from .serializers import PointShopSerializer


class PointShopViewSet(viewsets.ModelViewSet):
    queryset = PointShop.objects.all()
    serializer_class = PointShopSerializer
    permission_classes = [permissions.AllowAny]