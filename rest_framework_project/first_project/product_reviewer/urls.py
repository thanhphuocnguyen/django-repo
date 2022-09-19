from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageViewSet, ProductViewSet

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('images', ImageViewSet, basename='images')

urlpatterns = [
    path('', include(router.urls)),
]
