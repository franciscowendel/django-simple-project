from django.urls import path
from .views import (
    ProductsGenericsAPIView,
    ProductGenericAPIView,

    ProductViewSets,
)

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('products', ProductViewSets)

urlpatterns = [
    path('products/', ProductsGenericsAPIView.as_view(), name='products'),
    path('products/<int:pk>/', ProductGenericAPIView.as_view(), name='products_product'),
]
