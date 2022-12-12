from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ["pk", "name", "location", "photo", "description"]

class GetProductSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(many=False)
    class Meta:
        model = Product
        fields = ["pk", "name", "price", "photo", "provider"]


class PutProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["pk", "name", "price", "photo", "provider"]

class OrdersSerializer(serializers.ModelSerializer):
    product = GetProductSerializer(many = False)
    class Meta:
        model = Order
        fields = ["pk", "state", "quantity", "product"]

class ShCartSerializer(serializers.ModelSerializer):
    orders = OrdersSerializer(many=True)
    class Meta:
        model = ShoppingCart
        fields = ["pk", "address", "date", "orders"]

