from rest_framework import viewsets, permissions, generics

from tour_theme import serializers, models
from tour_theme.models import TourTheme
from tour_theme.serializers import TourThemeSerializer
from user.models import Profile


class TourThemeViewSet(viewsets.ModelViewSet):
    queryset = models.TourTheme.objects.all().order_by('-created')
    serializer_class = serializers.TourThemeSerializer
    permission_classes = [permissions.AllowAny]


class MyTourThemeList(generics.ListAPIView):
    serializer_class = TourThemeSerializer

    def get_queryset(self):
        user = self.request.user
        return TourTheme.objects.filter(author=Profile.objects.get(user=user))
