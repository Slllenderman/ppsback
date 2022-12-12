from .models import *
from django_filters import rest_framework as filters

class ProvidersFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    location = filters.CharFilter(field_name="location", lookup_expr="iexact")
    category = filters.ModelMultipleChoiceFilter(
        field_name="product__category",
        to_field_name="category",
        lookup_expr="iexact",
        queryset=Product.objects.all()
    )
    class Meta:
        models = Provider
        fields = ['category', 'name', 'location']

class ProductsFilter(filters.FilterSet):
    cost = filters.RangeFilter()
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'provider']