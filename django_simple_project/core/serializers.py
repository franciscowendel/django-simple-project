from rest_framework import serializers
from django_simple_project.core.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'stock',
            'created_at',
            'modified_at',
            'is_active'
        )
