from rest_framework import serializers
from api.models import Category, Image
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
      model = Category
      fields = ('id','title','description',)
class ImageSerializer(serializers.ModelSerializer):
   class Meta:
      model = Image
      fields = ('title','description','image','added_date','cat',)