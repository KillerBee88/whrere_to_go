from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place

MAX_IMAGE_HEIGHT = 200
MAX_IMAGE_WIDTH = 200


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 3
    readonly_fields = ['get_image_preview']
    fields = ('image', 'get_image_preview', 'order')

    def get_image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: {}px; max-height: {}px;"/>',
                obj.image.url,
                MAX_IMAGE_WIDTH,
                MAX_IMAGE_HEIGHT
            )
        return ''

    get_image_preview.short_description = "Превью"

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['location', 'image', 'order']
    list_filter = ['location']
    autocomplete_fields = ['location']


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'short_description', 'latitude', 'longitude']
