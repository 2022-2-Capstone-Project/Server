from rest_framework import viewsets, permissions
from . import models
from .serializers import TourSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = models.Tour.objects.all().order_by('-created')
    serializer_class = TourSerializer
    permission_classes = [permissions.AllowAny]