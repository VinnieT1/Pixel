from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('update_item/', views.update_item, name='update_item')
]