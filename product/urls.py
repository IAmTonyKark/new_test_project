from django.urls import path
from .views import product_list_create, index

urlpatterns = [
    path('api/product/', product_list_create, name='product_list_create'),
    path('', index, name='index'),
]