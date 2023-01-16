from django.urls import path
from .views import \
    index, \
    contact, \
    product, \
    ProductAPIView


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product'),

    path('products/', ProductAPIView.as_view(), name='products'),
]
