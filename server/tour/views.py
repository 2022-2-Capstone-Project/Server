from rest_framework import viewsets, permissions, generics

from user.models import Profile
from . import models
from .models import Tour
from .serializers import TourSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = models.Tour.objects.all().order_by('-created')
    serializer_class = TourSerializer
    permission_classes = [permissions.AllowAny]


class MyTourList(generics.ListAPIView):
    serializer_class = TourSerializer

    def get_queryset(self):
        user = self.request.user
        return Tour.objects.filter(profile=Profile.objects.get(user=user))


