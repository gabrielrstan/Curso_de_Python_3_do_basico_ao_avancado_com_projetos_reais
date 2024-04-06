import os

from PIL import Image
from django.conf import settings  # type: ignore
from django.db import models  # type: ignore
from utils.rands import slugify_new
from utils import utils


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField(max_length=2000)
    image = models.ImageField(
        upload_to='product_image/%y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    marketing_price = models.FloatField(verbose_name='Price')
    promotional_marketing_price = models.FloatField(
        default=0, verbose_name='Promotional Price')
    type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variable'),
            ('S', 'Simple'),
        )
    )

    def get_formatted_price(self):
        return utils.format_price(self.marketing_price)

    get_formatted_price.short_description = 'Price'  # type:ignore

    def get_formatted_promotional_price(self):
        return utils.format_price(self.promotional_marketing_price)

    get_formatted_promotional_price.short_description = 'Promotional Price'  # type:ignore  # noqa - E501

    @staticmethod
    def resize_image(img, image, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize(
            (new_width, new_height), Image.LANCZOS)  # pyright: ignore
        new_img.save(img_full_path, optimize=True, quality=60)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)

        super().save(*args, **kwargs)

        max_image_size = (800)

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self):
        return self.name


class Variation(models.Model):
    class Meta:
        verbose_name = 'Variation'
        verbose_name_plural = 'Variations'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField()
    promotional_price = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name or self.product.name
