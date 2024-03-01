from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from .models import Place, Image

class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 3
    readonly_fields = ['image_preview']
    fields = ('image', 'image_preview', 'order')

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px;"/>', obj.image.url) if obj.image else ''

    image_preview.short_description = "Превью"

@admin.register(Place)
class PlaceAdmin(SortableAdminBase,admin.ModelAdmin):
    inlines = [ImageInline]