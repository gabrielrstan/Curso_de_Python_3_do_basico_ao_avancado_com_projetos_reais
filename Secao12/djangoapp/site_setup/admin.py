from django.contrib import admin  # type: ignore
from site_setup.models import MenuLink, SiteSetup  # type: ignore


# @admin.register(MenuLink)
# class MenuLinkAdmin(admin.ModelAdmin):
#     list_display = 'id', 'text', 'url_or_path',
#     list_display_links = 'id', 'text', 'url_or_path',
#     search_fields = 'id', 'text', 'url_or_path',


class MenuLinkInLine(admin.TabularInline):
    model = MenuLink
    extra = 1


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',
    inlines = MenuLinkInLine,

    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()
