from django.urls import path
from .views import \
    index, \
    contact, \
    product, \
    ProductAPIView, \
    ProductsGenericsAPIView, \
    ProductGenericAPIView, \
    ProductViewSets

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('products', ProductViewSets)

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('product_registration/', product, name='product_registration'),

    path('products/', ProductAPIView.as_view(), name='products'),

    path('products/2/', ProductsGenericsAPIView.as_view(), name='products_2'),
    path('products/<int:pk>/', ProductGenericAPIView.as_view(), name='products_2_product'),
]
