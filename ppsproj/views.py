from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import *
from .filters import *
from .models import *
from .permissions import *

class Products(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
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
    permission_classes = [IsAuthenticatedOrReadOnly, IsProviderPermission, IsOneToOneProviderPermission]
    def get_serializer_class(self):
        if self.action == 'list':
            return GetProviderSerializer
        else:
            return PutProviderSerializer
    def create(self, request):
        username = request.GET.get('username', '')
        user = User.objects.get(username=username).pk
        request.data.update({'user' : user})
        return super().create(request)
        
class Orders(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    filterset_class = OrdersFilter
    permission_classes = [IsAuthenticated, IsOrderOwnerPermission]
    def get_serializer_class(self):
        if self.action == 'list':
            return GetOrdersSerializer
        else:
            return PutOrdersSerializer

class ShoppingCart(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    filterset_class = ShCartFilter
    serializer_class = ShCartSerializer
    permission_classes = [IsAuthenticated, IsShCartOwnerPermission]
    def create(self, request):
        username = request.GET.get('username', '')
        customer = User.objects.get(username=username).pk
        request.data.update({'customer' : customer})
        return super().create(request)

class IsAuthenticated(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"Authenticated" : "true"})



