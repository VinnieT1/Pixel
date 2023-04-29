from django.shortcuts import render, redirect
from .models import Product
from cart.models import Order
# Create your views here.
def product_view(request, pk):
    context = {
        'pk':pk,
    }

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        context['num_cart_items'] = order.get_cart_items

    return render(request, 'product.html', context)

def products_view(request):
    products = Product.objects.order_by('-created_at')
    context = {
        'products':products,
    }

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        context['num_cart_items'] = order.get_cart_items

    return render(request, 'products.html', context)

def products_type_view(request, product_type):
    if product_type not in ['CPU', 'GPU', 'PC']:
        return redirect('products')

    products = Product.objects.filter(product_type=product_type)
    context = {
        'products':products,
        'product_type':product_type,
    }
    
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        context['num_cart_items'] = order.get_cart_items

    return render(request, 'products.html', context)