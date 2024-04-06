from django.contrib import admin  # type: ignore
from order.models import Order, OrderedItem


class OrderedItemInline(admin.TabularInline):
    model = OrderedItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderedItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedItem)
