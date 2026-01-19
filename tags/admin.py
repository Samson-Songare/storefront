from django.contrib import admin
from .models import Tag

# Tab model

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['label']

