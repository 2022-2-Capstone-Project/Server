from rest_framework import viewsets, permissions, generics

from django.contrib import messages
from django.db.models import Q
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


class SearchTour(generics.ListAPIView):
    serializer_class = TourSerializer

    def get_queryset(self):
        keyword = self.request.GET.get("keyword", "")
        print(f"keyword = {keyword}")

        if len(keyword) < 2:
            # 프런트에서 2글자 미만인 검색이 들어오는 것을 막아야함
            return messages.error(self.request, "검색어는 2글자 이상 입력해주세요.")

        return Tour.objects.filter(
            Q(tourName__icontains=keyword) |
            Q(description__icontains=keyword))
