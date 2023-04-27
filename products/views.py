from django.shortcuts import render
from .models import Product
# Create your views here.
def product_view(request, pk):
    return render(request, 'product.html', {'pk':pk})

def products_view(request):
    products = Product.objects.order_by('-created_at')
    return render(request, 'products.html', {'products':products})

def products_type_view(request, product_type):
    return render(request, 'products.html', {'product_type':product_type})