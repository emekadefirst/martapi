from rest_framework import serializers
from models.category_model import Category
from models.buyer_model import Buyer
from models.product_model import Product
from models.cart_model import Cart
from models.History_model import History
from models.wallet_model import Wallet
from models.order_model import Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = "__all__"