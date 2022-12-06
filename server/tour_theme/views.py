from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib import messages
from django.db.models import Q

from tour_theme import serializers, models
from tour_theme.models import TourTheme
from tour_theme.serializers import TourThemeSerializer
from user.models import Profile

# class TourThemeList(APIView):
#     """
#     List all tour themes, or create a new tour theme.
#     """
#     def get(self, request, format=None):
#         tour_themes = TourTheme.objects.all()
#         serializers = TourThemeSerializer(tour_themes, many=True)
#         return Response(serializers.data)

#     def post(self, request, format=None):
#         serializer = TourThemeSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(request.user, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TourThemeViewSet(viewsets.ModelViewSet):
    queryset = models.TourTheme.objects.all().order_by('-created')
    serializer_class = serializers.TourThemeSerializer
    permission_classes = [permissions.AllowAny]


class MyTourThemeList(generics.ListAPIView):
    serializer_class = TourThemeSerializer

    def get_queryset(self):
        user = self.request.user
        print(f"user {user}")
        my_profile = Profile.objects.filter(username=user)
        print(my_profile)

        return TourTheme.objects.filter(author__in=my_profile)


class SearchTourTheme(generics.ListAPIView):
    serializer_class = TourThemeSerializer

    def get_queryset(self):
        keyword = self.request.GET.get("keyword", "")
        print(f"keyword = {keyword}")
        if len(keyword) < 2:
            # 프런트에서 2글자 미만인 검색이 들어오는 것을 막아야함
            return messages.error(self.request, "검색어는 2글자 이상 입력해주세요.")

        return TourTheme.objects.filter(
            Q(title__icontains=keyword) |
            Q(description__icontains=keyword))
