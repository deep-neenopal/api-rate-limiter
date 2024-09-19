from django.urls import path
from .views import product_list_create_view, product_detail_view

urlpatterns = [
    path('', product_list_create_view, name='product-list-create'),  # List and Create products
    path('<int:pk>/', product_detail_view, name='product-detail'),  # Retrieve product by ID
]
