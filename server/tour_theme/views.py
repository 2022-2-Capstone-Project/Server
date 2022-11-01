from rest_framework import viewsets, permissions

from tour_theme import serializers, models


class TourThemeViewSet(viewsets.ModelViewSet):
    queryset = models.TourTheme.objects.all().order_by('-created')
    serializer_class = serializers.TourThemeSerializer
    permission_classes = [permissions.AllowAny]
