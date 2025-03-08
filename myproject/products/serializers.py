from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id', 'name', 'description', 'category', 'price', 'brand', 'quantity']

    def validate_price(self, value):
        if value>1000:
            raise serializers.ValidationError("price should be less than 1000")
        return value