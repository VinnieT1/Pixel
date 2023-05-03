from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('update_item/', views.update_item, name='update_item'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('complete/', views.purchase_complete_view, name='purchase_complete'),
]