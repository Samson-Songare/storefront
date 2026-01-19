from django.contrib import admin
from store.admin import ProductAdmin
from tags.models import TagItem
from django.contrib.contenttypes.admin import GenericTabularInline
from store.models import Product


class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    extra = 0
    min_num = 1
    max_num = 10
    model = TagItem


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
