from django.contrib import admin  # type: ignore
from product.models import Product, Variation


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [VariationInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)

# Register your models here.
