from django.urls import path

from api.views.product import ProductViewSet
from api.views.buyer import RegisterUserView, LoginView
from api.views.cart import CartView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', LoginView.as_view()),
    path('cart/', CartView.as_view()),
    path('product/', ProductViewSet.as_view())
    
]