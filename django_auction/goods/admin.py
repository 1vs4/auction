from django.contrib import admin

from goods.models import Product, Order


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'expiration')
    fields = ('name', 'description', ('price', 'quantity'), 'image1', 'image2', 'expiration', 'user', 'is_active')
    search_fields = ('name',)
    ordering = ('expiration',)

@admin.register(Order)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user',)
    ordering = ('user',)