from rest_framework import serializers
from .models import TourApplication


class TourApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourApplication
        fields = '__all__'
