from django.urls import include, path
from rest_framework import routers
from api.views import CategoryViewSet, ImageViewSet
router = routers.DefaultRouter()
router.register(r'Category', CategoryViewSet)
router.register(r'Image', ImageViewSet)
urlpatterns = [
   path('', include(router.urls)),
]