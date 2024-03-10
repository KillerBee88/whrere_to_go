from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from .models import Place, Image

MAX_IMAGE_HEIGHT = 200
MAX_IMAGE_WIDTH = 200

class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 3
    readonly_fields = ['generate_image_html']
    fields = ('image', 'generate_image_html', 'order')

    def generate_image_html(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: {}px; max-height: {}px;"/>',
                obj.image.url,
                MAX_IMAGE_WIDTH,
                MAX_IMAGE_HEIGHT
            )
        return ''

    generate_image_html.short_description = "Превью"

class ImageAdmin(admin.ModelAdmin):
    list_display = ['location', 'image', 'order']
    list_filter = ['location']

admin.site.register(Image, ImageAdmin)

@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
