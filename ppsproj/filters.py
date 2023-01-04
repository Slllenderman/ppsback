from .models import *
from django_filters import rest_framework as filters
from django.contrib.auth.models import User

class ProvidersFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    location = filters.CharFilter(field_name="location", lookup_expr="icontains")
    category = filters.ModelMultipleChoiceFilter(
        field_name="product__category",
        to_field_name="category",
        lookup_expr="iexact",
        queryset=Product.objects.all()
    )
    username = filters.ModelMultipleChoiceFilter(
        field_name="user__username",
        to_field_name="username",
        lookup_expr="exact",
        queryset=User.objects.all()
    )
    class Meta:
        models = Provider
        fields = ['category', 'name', 'location', 'username']

class ProductsFilter(filters.FilterSet):
    price = filters.RangeFilter()
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'provider']

class OrdersFilter(filters.FilterSet):
    provider = filters.CharFilter(field_name='product__provider', lookup_expr='exact')
    class Meta:
        model = Order
        fields = ['shCart', 'provider']

class ShCartFilter(filters.FilterSet):
    id = filters.CharFilter(field_name='id', lookup_expr='icontains')
    location = filters.CharFilter(field_name="address", lookup_expr="icontains")
    date = filters.DateFilter(field_name="date")
    username = filters.ModelMultipleChoiceFilter(
        field_name='customer__username', 
        to_field_name='username',
        lookup_expr="exact",
        queryset=User.objects.all() 
    )
    state = filters.ChoiceFilter(choices=ShoppingCart.STATES)
    class Meta:
        model = ShoppingCart
        fields = ['id', 'username', 'location', 'date', 'state']