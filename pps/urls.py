from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from ppsproj import views as pps_views

router = routers.DefaultRouter()
router.register(r'products', pps_views.Products)
router.register(r'providers', pps_views.Providers)

urlpatterns = [
    path('', include(router.urls)),
    path(r'auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('auth/IsAuthenticated', pps_views.IsAuthenticated.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
