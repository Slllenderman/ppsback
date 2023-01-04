from rest_framework import permissions
from .models import *


class OrderOwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if(request.user.is_superuser): 
            return True
        pk = request.GET.get('shCart', '')
        provider = request.GET.get('provider', '')
        if(provider == ''):
            if(pk == ''): 
                return False
            cart = ShoppingCart.objects.get(pk=pk)
            return cart.customer.username == request.user.username
        else:
            provider = Provider.objects.get(pk=provider)
            return provider.user.username == request.user.username


class ShCartOwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if(request.user.is_superuser):
            return True
        if(request.method == 'PUT'):
            try:
                cartId = request.GET.get('shCart', '')
                cart = ShoppingCart.objects.get(id=cartId)
                return cart.customer.username == request.user.username
            except:
                return False
        else:
            provider = request.GET.get('provider', '')
            if(provider == ''):
                username = request.GET.get('username', '')
                return username == request.user.username
            else:
                provider = Provider.objects.get(pk=provider)
                return provider.user.username == request.user.username


class IsProviderPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        username = request.GET.get('username', '')
        if(username != ''):
            if(request.user.is_superuser):
                return True
            return username == request.user.username
        else:
            return True


class IsOneToOneProviderPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if(request.method == 'POST'):
            username = request.GET.get('username', '')
            if(username == ''): return False
            try:
                user = User.objects.get(username=username)
                try:
                    provider = Provider.objects.get(user=user.pk)
                    return False
                except Provider.DoesNotExist:
                    return True
            except User.DoesNotExist:
                return False
        else:
            return True


class StatusPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PUT':
            status = request.GET.get('status', '')
            if status != 'R' and status != 'A' : return False
            else : return True
        else:
            return True 