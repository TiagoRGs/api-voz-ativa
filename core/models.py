from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    class Meta:
        verbose_name = _("Categoria")
        verbose_name_plural = _("Categorias")

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Upload/Category', name="category_image", blank=True, null=True)


    is_initial = models.BooleanField(
        verbose_name="Setup Inicial",
        null=False,
        blank=False,
        default=False,
        editable=True,
    )

    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_category = models.BooleanField(
        verbose_name="is_categoria",
        null=False,
        blank=False,
        default=True,
        editable=False,
    )

    def __str__(self):
        return self.name

class Image(models.Model):
    class Meta:
        verbose_name = _("Imagem")
        verbose_name_plural = _("Imagens")


    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Upload/Images', verbose_name="Imagem",  blank=True, null=True)

    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name