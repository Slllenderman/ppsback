from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .filters import *
from .models import *

class Products(viewsets.ModelViewSet):
    filterset_class = ProductsFilter
    queryset = Product.objects.filter(state='S')
    def get_serializer_class(self):
        if self.action == 'list':
            return GetProductSerializer
        else:
            return PutProductSerializer

class Providers(viewsets.ModelViewSet):
    filterset_class = ProvidersFilter
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class IsAuthenticated(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"Authenticated" : "true"})



class ShoppingCart(viewsets.ViewSet):
    def list(self, request, pk):
        queryset = ShoppingCart.objects.filter(pk=pk)
        serializer = ShCartSerializer(queryset)
        return Response(serializer.data)


