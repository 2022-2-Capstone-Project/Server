from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from requests import Response
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from tour_application import serializers, models

from tour.models import Tour
from .models import TourApplication
from .serializers import TourApplicationSerializer
from user.models import Profile


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
        print(f"tour_application = {tour_application}")

        user_id = self.request.user.id

        tour_application.user.add(user_id)
        print(f"tour_application.user = {tour_application.user}")
        tour_application.participants_on_site = tour_application.user.count()

        serializer = TourApplicationSerializer(tour_application, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(data=serializer.data)

        return JsonResponse(data="wrong parameters")



class EarnPoint(APIView):
    serializer_class = serializers.TourApplicationSerializer

    def patch(self, request, tour_id):

        tour = Tour.objects.get(pk=tour_id)
        print(f"tour = {tour}")
        tour_application = TourApplication.objects.get(tour=tour)
        print(f"tour_application = {tour_application}")

        print(f"tour_application.user = {tour_application.user}")
        for user in tour_application.user:
            profile = Profile.objects.get(pk=user)
            profile.point += 100

            serializer = serializers.ProfileSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

        tour = Tour.objects.filter(tour_application__in=tour_application)
        print(f"투어 신청서로 찾은 투어 = {tour}")

        sr = Profile.objects.filter(id__in=tour.profile_id)
        print(f"투어로 찾은 선배 = {sr}")
        sr.point += 100
        serializer = serializers.ProfileSerializer(sr, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(data=serializer.data)

        return JsonResponse(data="wrong parameters")