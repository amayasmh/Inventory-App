from django.contrib import admin

# Register your models here.
from inv.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('reference', 'brand', 'date_exp')
    list_filter = ('reference', 'date_exp')
    search_fields = ('reference', 'date_exp')