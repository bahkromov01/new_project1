from django.contrib import admin
from django.urls import path, include
from app.views import ProductlistView, ProductDetailView, AddProductView, DeleteProductView
from . import views
urlpatterns = [
    path('index/', ProductlistView.as_view(), name='index'),
    path('product_detail/<int:product_id>', ProductDetailView.as_view() , name='product_detail'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('delete_product/', DeleteProductView.as_view(), name='delete_product')


]