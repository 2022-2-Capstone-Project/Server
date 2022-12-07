from rest_framework import serializers
from .models import PointShop

class PointShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = PointShop
        fields = '__all__'