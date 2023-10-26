from django.contrib import admin

from goods.models import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'expiration')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'expiration')
    search_fields = ('name',)
    ordering = ('expiration',)