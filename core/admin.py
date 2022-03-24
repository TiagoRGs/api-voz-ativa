from django.contrib import admin
from .models import Image, Category

@admin.register(Category)  
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_initial', 'create_at', 'updated_at')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'create_at', 'updated_at')
