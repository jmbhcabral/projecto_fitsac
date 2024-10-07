from django.contrib import admin
from .models import (
    SectionOne, SectionTwo, SectionThree, SectionFour, SectionSix,
    SectionEight, SectionNine, PricingOffers, PriceCardIcons,
    OffersIcons, SectionFiveHeader, Card, TiposDeAulas
)


class SectionOneAdmin(admin.ModelAdmin):
    list_display = ('name', 'text_field_1', 'text_field_2',
                    'is_visible', 'created_at', 'updated_at')
    search_fields = ('name', 'text_field_1', 'text_field_2',
                     'is_visible', 'created_at', 'updated_at')
    list_filter = ('name', 'text_field_1', 'text_field_2',
                   'is_visible', 'created_at', 'updated_at')
    list_editable = ('is_visible',)


class SectionTwoAdmin(admin.ModelAdmin):
    list_display = ('name', 'text_field_3', 'text_field_4',
                    'image_1', 'image_2', 'is_visible',
                    'created_at', 'updated_at')
    search_fields = ('name', 'text_field_3', 'text_field_4',
                     'image_1', 'image_2', 'is_visible',
                     'created_at', 'updated_at')
    list_filter = ('name', 'text_field_3', 'text_field_4',
                   'image_1', 'image_2', 'is_visible',
                   'created_at', 'updated_at')
    list_editable = ('is_visible',)


class SectionThreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'text_field_1', 'text_field_2',
                    'url_or_path_1', 'is_visible',
                    'created_at', 'updated_at')
    search_fields = ('name', 'text_field_1', 'text_field_2',
                     'url_or_path_1', 'is_visible',
                     'created_at', 'updated_at')
    list_filter = ('name', 'text_field_1', 'text_field_2',
                   'url_or_path_1', 'is_visible',
                   'created_at', 'updated_at')
    list_editable = ('url_or_path_1', 'is_visible')


class SectionFourAdmin(admin.ModelAdmin):
    list_display = ('tag', 'image', 'is_visible',
                    'order', 'created_at', 'updated_at')
    search_fields = ('tag', 'image', 'is_visible',
                     'order', 'created_at', 'updated_at')
    list_filter = ('tag', 'image', 'is_visible',
                   'order', 'created_at', 'updated_at')
    list_editable = ('is_visible', 'order')


class SectionSixAdmin(admin.ModelAdmin):
    list_display = ('name', 'paragraph_1', 'paragraph_2',
                    'is_visible', 'created_at', 'updated_at')
    search_fields = ('name', 'paragraph_1', 'paragraph_2',
                     'is_visible', 'created_at', 'updated_at')
    list_filter = ('name', 'paragraph_1', 'paragraph_2',
                   'is_visible', 'created_at', 'updated_at')
    list_editable = ('is_visible',)


class SectionEightAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_url',
                    'created_at', 'updated_at', 'is_visible')
    search_fields = ('name', 'video_url',
                     'created_at', 'updated_at', 'is_visible')
    list_filter = ('name', 'video_url',
                   'created_at', 'updated_at', 'is_visible')
    list_editable = ('is_visible',)


class SectionNineAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'text_field_1', 'text_field_2',
                    'is_visible', 'order', 'created_at', 'updated_at')
    search_fields = ('name', 'icon', 'text_field_1', 'text_field_2',
                     'is_visible', 'order', 'created_at', 'updated_at')
    list_filter = ('name', 'icon', 'text_field_1', 'text_field_2',
                   'is_visible', 'order', 'created_at', 'updated_at')
    list_editable = ('is_visible', 'order')


class PricingOffersAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible', 'created_at', 'updated_at')
    search_fields = ('name', 'is_visible', 'created_at', 'updated_at')
    list_filter = ('name', 'is_visible', 'created_at', 'updated_at')
    list_editable = ('is_visible',)


class PriceCardIconsAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'is_visible', 'created_at', 'updated_at')
    search_fields = ('name', 'icon', 'is_visible', 'created_at', 'updated_at')
    list_filter = ('name', 'icon', 'is_visible', 'created_at', 'updated_at')
    list_editable = ('is_visible',)


class OffersIconsAdmin(admin.ModelAdmin):
    list_display = ('offer', 'icon', 'is_visible',
                    'created_at', 'updated_at')
    search_fields = ('offer', 'icon', 'is_visible',
                     'created_at', 'updated_at')
    list_filter = ('offer', 'icon', 'is_visible',
                   'created_at', 'updated_at')
    list_editable = ('is_visible',)


class SectionFiveHeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible', 'created_at', 'updated_at')
    search_fields = ('name', 'is_visible', 'created_at', 'updated_at')
    list_filter = ('name', 'is_visible', 'created_at', 'updated_at')
    list_editable = ('is_visible',)


class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'price', 'span',
                    'is_visible', 'order', 'created_at', 'updated_at')
    search_fields = ('name', 'logo', 'price', 'span',
                     'is_visible', 'order', 'created_at', 'updated_at')
    list_filter = ('name', 'logo', 'price', 'span',
                   'is_visible', 'order', 'created_at', 'updated_at')
    list_editable = ('is_visible', 'order')


class TiposDeAulasAdmin(admin.ModelAdmin):
    ''' Admin class for the TiposDeAulas model. '''
    list_display = ['tipo', 'description', 'image', 'order', 'is_visible']
    search_fields = ['tipo', 'description', 'image']
    list_filter = ['tipo', 'description', 'image']
    list_editable = ['is_visible', 'order']
    list_per_page = 10


admin.site.register(SectionOne, SectionOneAdmin)
admin.site.register(SectionTwo, SectionTwoAdmin)
admin.site.register(SectionThree, SectionThreeAdmin)
admin.site.register(SectionFour, SectionFourAdmin)
admin.site.register(SectionSix, SectionSixAdmin)
admin.site.register(SectionEight, SectionEightAdmin)
admin.site.register(SectionNine, SectionNineAdmin)
admin.site.register(PricingOffers, PricingOffersAdmin)
admin.site.register(PriceCardIcons, PriceCardIconsAdmin)
admin.site.register(OffersIcons, OffersIconsAdmin)
admin.site.register(SectionFiveHeader, SectionFiveHeaderAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(TiposDeAulas, TiposDeAulasAdmin)
