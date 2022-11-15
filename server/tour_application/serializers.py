from rest_framework import serializers
from .models import TourApplication


class TourApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TourApplication
        fields = '__all__'
