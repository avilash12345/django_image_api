from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from api.serializers import CategorySerializer, ImageSerializer
from api.models import Category, Image


class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


