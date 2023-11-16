from django.shortcuts import render
from rest_framework.decorators import APIView
from .models.category_model import Category
from .models.buyer_model import Buyer, Cart
from .models.product_model import Product
from rest_framework.response import Response
from rest_framework.response import Response
from .serializers.buyer_serializer import BuyerSerializer, UserSerializer, DeliveryAddressSerializer
from .serializers.cart_serializer import CartSerializer
from .serializers.category_serializer import CategorySerializer
from .serializers.history_serializer import HistorySerializer
from .serializers.order_serializer import OrderSerializer
from .serializers.product_serializer import ProductSerializer
from rest_framework import status
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.signals import user_logged_in
from django.db.models import Q
from django.dispatch import receiver
from rest_framework.permissions import AllowAny
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from .models.order_model import Order