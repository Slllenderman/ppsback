from rest_framework import permissions
from .models import *


class IsOrderOwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if(request.user.is_superuser): 
            return True
        pk = request.GET.get('shCart', '')
        if(pk == ''): 
            return False
        cart = ShoppingCart.objects.get(pk=pk)
        return cart.customer.username == request.user.username

    def has_object_permission(self, request, view, obj):
        return False

class IsShCartOwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if(request.user.is_superuser):
            return True
        username = request.GET.get('username', '')
        return username == request.user.username

class IsProviderPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        username = request.GET.get('username', '')
        if(username != ''):
            if(request.user.is_superuser):
                return True
            return username == request.user.username
        else:
            return True