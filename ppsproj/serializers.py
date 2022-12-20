from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class PutProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ["pk", "name", "location", "photo", "description", "user"]

class GetProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ["pk", "name", "location", "photo", "description"]

class GetProductSerializer(serializers.ModelSerializer):
    provider = GetProviderSerializer(many=False)
    class Meta:
        model = Product
        fields = ["pk", "name", "price", "photo", "provider"]


class PutProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["pk", "name", "price", "photo", "provider"]

class GetOrdersSerializer(serializers.ModelSerializer):
    product = GetProductSerializer(many = False)
    class Meta:
        model = Order
        fields = ["pk", "state", "quantity", "product"]


class PutOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["pk", "quantity", "product", "shCart"]

class ShCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ["pk", "address", "date", "state", "customer"]

