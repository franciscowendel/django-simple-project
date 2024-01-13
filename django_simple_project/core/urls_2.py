from django.urls import path
from .views import (
    ProductAPIView,

    ProductsGenericsAPIView,
    ProductGenericAPIView,

    ProductViewSets,
)

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('products', ProductViewSets)

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='products'),

    path('products/2/', ProductsGenericsAPIView.as_view(), name='products_2'),
    path('products/<int:pk>/', ProductGenericAPIView.as_view(), name='products_2_product'),
]
