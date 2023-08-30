from rest_framework import serializers
from .models import Ad, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class AdSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)

    class Meta:
        model = Ad
        fields = '__all__'
