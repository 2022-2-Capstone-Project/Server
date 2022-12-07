from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from tour_application import serializers, models

from tour.models import Tour
from .models import TourApplication
from .serializers import TourApplicationSerializer


class TourApplicationViewSet(viewsets.ModelViewSet):
    queryset = models.TourApplication.objects.all().order_by('-created')
    serializer_class = serializers.TourApplicationSerializer
    permission_classes = [permissions.AllowAny]


class AddParticipant(APIView):
    serializer_class = serializers.TourApplicationSerializer

    def patch(self, request, tour_id):
        tour = Tour.objects.get(pk=tour_id)
        print(f"tour = {tour}")
        tour_application = TourApplication.objects.get(tour=tour)

        # tour_application = self.get_object(pk)
        user_id = self.request.user.id

        tour_application.user.add(user_id)
        tour_application.participants_on_site = tour_application.user.count()

        serializer = TourApplicationSerializer(tour_application, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(data=serializer.data)

        return JsonResponse(data="wrong parameters")


class EarnPoint(APIView):
    serializer_class = serializers.TourApplicationSerializer

    def patch(self, request, pk):
        user = Tour.objects.get(pk=pk)
        tour.status = 3

        serializer = TourSerializer(tour, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(data=serializer.data)

        return JsonResponse(data="wrong parameters")