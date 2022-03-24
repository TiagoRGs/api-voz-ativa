from .models import Image, Category
from .serializers import ImageSerializer
from .serializers import CategorySerializer

from rest_framework import viewsets

class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ImageSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Image.objects.filter(category = category)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GalleryAllViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

