from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .pagination import StandardResultsSetPagination

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all().order_by('name')
    serializer_class=ProductSerializer
    pagination_class=StandardResultsSetPagination