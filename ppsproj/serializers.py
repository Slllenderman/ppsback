from .models import *
from rest_framework import serializers

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ["pk", "name", "city", "photo", "description"]

class ProductSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(many=False)
    class Meta:
        model = Product
        fields = ["pk", "name", "cost", "photo", "provider"]
