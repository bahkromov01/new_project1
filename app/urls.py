from django.contrib import admin
from django.urls import path, include
from app.views import index, product_detail, add_product
from . import views
urlpatterns = [
    path('index/', index, name='index'),
    path('product_detail/<int:product_id>', product_detail, name='product_detail'),
    path('add_product/', add_product, name='add_product'),

]