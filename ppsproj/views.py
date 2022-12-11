from rest_framework import viewsets, views
from django_filters import rest_framework as filters
from .serializers import *
from .models import *

class ProductsFilter(filters.FilterSet):
    cost = filters.RangeFilter()
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    class Meta:
        model = Product
        fields = ['category', 'name', 'cost', 'provider']

class GetProducts(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductsFilter


class ProvidersFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    city = filters.CharFilter(field_name="city", lookup_expr="iexact")
    category = filters.ModelMultipleChoiceFilter(
        field_name="product__category",
        to_field_name="category",
        lookup_expr="iexact",
        queryset=Product.objects.all()
    )
    class Meta:
        models = Provider
        fields = ['category', 'name', 'city']

class GetProviders(viewsets.ReadOnlyModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filterset_class = ProvidersFilter
    
