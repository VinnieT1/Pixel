from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products_view, name='all_products'),
    path('<int:pk>', views.product_view, name='product'),
    path('<str:product_type>', views.products_type_view, name='products_type'),
    path('register/', views.register_product_view, name='create_product'),
]