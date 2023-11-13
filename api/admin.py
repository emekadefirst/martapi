from django.contrib import admin
from .models.category_model import Category
from .models.buyer_model import Buyer
from .models.product_model import Product
from .models.cart_model import Cart
from .models.History_model import History
from .models.wallet_model import Wallet
from .models.order_model import Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity']
    list_filter = ['category']
    search_fields = ['name']


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'wallet_balance', 'LGA', 'state']
    list_filter = ['LGA', 'state']
    search_fields = ['user__username']


class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'cost', 'quantity', 'time_added']

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'cart', 'total_purchase', 'time_purchased']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'reference', 'status']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Order, OrderAdmin)
