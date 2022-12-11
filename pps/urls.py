from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from ppsproj import views as pps_views

router = routers.DefaultRouter()
router.register(r'getProducts', pps_views.GetProducts)
router.register(r'getProviders', pps_views.GetProviders)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
