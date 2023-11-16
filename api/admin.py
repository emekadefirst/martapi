from django.contrib import admin
from api.models.category_model import Category
from api.models.buyer_model import Buyer, Order
from api.models.product_model import Product, ProductImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductImageInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = ProductImage
    extra = 1  # Number of empty forms to display for adding new images

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity']
    list_filter = ['category']
    search_fields = ['name']
    inlines = [ProductImageInline]  # Include the inline for ProductImage

class BuyerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'wallet_balance', 'date_created')
    search_fields = ['user__username', 'phone_number']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'reference', 'status']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Order, OrderAdmin)
