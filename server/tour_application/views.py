from rest_framework import viewsets, permissions
from tour_application import serializers, models


class TourApplicationViewSet(viewsets.ModelViewSet):
    queryset = models.TourApplication.objects.all().order_by('-created')
    serializer_class = serializers.TourApplicationSerializer
    permission_classes = [permissions.AllowAny]