from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

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
        return TourTheme.objects.filter(author=Profile.objects.get(user=user))
