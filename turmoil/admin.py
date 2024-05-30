from django.contrib import admin
from .models import Article, Slider
from image_cropping import ImageCroppingMixin
from django.utils.html import format_html

class CustomAdminMixin:
    class Media:
        js = ('js/image_preview.js',)

@admin.register(Article)
class ArticleAdmin(CustomAdminMixin, ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    search_fields = ('title', 'subtitle', 'author')
    readonly_fields = ('thumbnail_preview', 'image_preview')

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" width="61" height="47" />'.format(obj.thumbnail_cropped.url))
        return ""
    thumbnail_preview.short_description = 'Thumbnail Preview'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="598" height="134" />'.format(obj.image_cropped.url))
        return ""
    image_preview.short_description = 'Image Preview'

@admin.register(Slider)
class SliderAdmin(CustomAdminMixin, ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('slide_title', 'created_at')
    search_fields = ('slide_title', 'side_title')
    readonly_fields = ('slide_image_preview', 'side_image_preview')

    def slide_image_preview(self, obj):
        if obj.slide_image:
            return format_html('<img src="{}" width="705" height="298" />'.format(obj.slide_image_cropped.url))
        return ""
    slide_image_preview.short_description = 'Slide Image Preview'

    def side_image_preview(self, obj):
        if obj.side_image:
            return format_html('<img src="{}" width="47" height="50" />'.format(obj.side_image_cropped.url))
        return ""
    side_image_preview.short_description = 'Side Image Preview'
