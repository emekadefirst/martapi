from django.contrib import admin
from api.models.category_model import Category
from api.models.buyer_model import Buyer
from api.models.product_model import Product
from api.models.buyer_model import Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity']
    list_filter = ['category']
    search_fields = ['name']


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'token', 'phone_number', 'wallet_balance', 'LGA', 'state', 'cart', 'history']  # Include 'cart'
    list_filter = ['LGA', 'state']
    search_fields = ['user__username']


class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'reference', 'status']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Order, OrderAdmin)
