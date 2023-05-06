from django.shortcuts import render, redirect
from .models import Product
from cart.models import Order
from users.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def product_view(request, pk):
    product = Product.objects.get(pk=pk)

    context = {
        'pk':pk,
        'product':product,
    }

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        context['num_cart_items'] = order.get_cart_items

    context['register_form'] = UserCreationForm()
    context['login_form'] = AuthenticationForm()

    return render(request, 'product.html', context)

def products_view(request, query=None):
    if query:
        products = Product.objects.filter(title__icontains=query).order_by('-created_at')
    else:
        products = Product.objects.order_by('-created_at')

    context = {
        'products':products,
    }

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        context['num_cart_items'] = order.get_cart_items

    context['register_form'] = UserCreationForm()
    context['login_form'] = AuthenticationForm()

    return render(request, 'products.html', context)

def products_type_view(request, product_type):
    if product_type not in ['CPU', 'GPU', 'PC']:
        return redirect('home')

    products = Product.objects.filter(product_type=product_type)
    context = {
        'products':products,
        'product_type':product_type,
    }
    
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        context['num_cart_items'] = order.get_cart_items

    context['register_form'] = UserCreationForm()
    context['login_form'] = AuthenticationForm()

    return render(request, 'products.html', context)

def search(request):
    query = request.GET.get('query')
    return products_view(request, query)