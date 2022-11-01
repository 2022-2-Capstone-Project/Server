from django.contrib.auth.models import User, Permission
from rest_framework import serializers

from .models import TourTheme


class TourThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TourTheme
        fields = '__all__'
