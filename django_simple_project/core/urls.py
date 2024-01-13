from django.urls import path
from .views import \
    index, \
    contact, \
    product, \
    ProductViewSets

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('product_registration/', product, name='product_registration'),

]