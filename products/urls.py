from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view, name='products'),
    path('<int:pk>', views.product_view, name='product'),
    path('<str:product_type>', views.products_type_view, name='products_type'),
    path('search/', views.search, name='search'),
]