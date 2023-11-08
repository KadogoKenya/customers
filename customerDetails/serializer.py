from rest_framework import serializers
from .models import LocationDetails,Business


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationDetails
        fields= "__all__"

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields= "__all__"