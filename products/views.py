from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from .throttles import ProductDetailThrottle, ProductThrottle


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [ProductThrottle]


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [ProductDetailThrottle]
