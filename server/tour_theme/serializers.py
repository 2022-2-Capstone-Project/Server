from django.contrib.auth.models import User, Permission
from rest_framework import serializers

from .models import TourTheme


class TourThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TourTheme
        fields = '__all__'


# class TourThemeSerializer(serializers.Serializer):
#     title = serializers.CharField(required=True, max_length=100)
#     estimated = serializers.IntegerField(required=True)
#     participants = serializers.IntegerField(required=True)
#     start_place = serializers.CharField(required=True, max_length=100)
#     latitude = serializers.FloatField(required=True)
#     longitude = serializers.FloatField(required=True)
#     thumbnail = serializers.ImageField(required=False)
#     checkpoints = serializers.CharField(required=False)

#     def create(self, validated_data):
#         checkpoints = 'test'
#         return TourTheme.objects.create(checkpoints=checkpoints, **validated_data)

#     def update(self, instance, validated_data):
#         return super().update(instance, validated_data)
