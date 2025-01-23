"""
URL configuration for drfpet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shop.views import HardwareViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'shop', HardwareViewSet, basename='shop')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/drfauth/', include('rest_framework.urls')),
    # path('api/v1/shop_list/', HardwareViewSet.as_view({'get': 'list'})),
    # path('api/v1/shop_list/<int:pk>/', HardwareViewSet.as_view({'put': 'update'})),
]
