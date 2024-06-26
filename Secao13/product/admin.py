from django.contrib import admin  # type: ignore

from product.models import Product, Variation


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_formatted_price',
                    'get_formatted_promotional_price',)
    inlines = [VariationInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)

# Register your models here.
