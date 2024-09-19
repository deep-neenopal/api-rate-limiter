from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from .throttles import GetProductThrottle, PostProductThrottle, ProductDetailThrottle
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
# @throttle_classes([PostProductThrottle, GetProductThrottle])  # Utilizing ProductThrottle for list and create
@throttle_classes([PostProductThrottle, GetProductThrottle])  # Utilizing ProductThrottle for list and create
def product_list_create_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@throttle_classes([ProductDetailThrottle])  # Utilizing ProductDetailThrottle for retrieving
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
