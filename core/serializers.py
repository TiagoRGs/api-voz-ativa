from rest_framework import serializers
from .models import Image, Category

class ImageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
  
    class Meta:
        model = Image
        fields = '__all__'
    

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)

    class Meta:
        model = Category
        fields = '__all__'
    