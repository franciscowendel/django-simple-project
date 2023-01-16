from django.urls import path
from .views import \
    index, \
    contact, \
    product, \
    ProductAPIView, \
    ProductsGenericsAPIView, \
    ProductGenericAPIView


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product'),

    path('products/', ProductAPIView.as_view(), name='products'),

    path('products/2/', ProductsGenericsAPIView.as_view(), name='products_2'),
    path('products/<int:pk>/', ProductGenericAPIView.as_view(), name='products_2_product'),
]
