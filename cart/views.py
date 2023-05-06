import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from products.models import Product
from .forms import ShippingAdressForm

# Create your views here.
def cart_view(request):
    print('alo')
    if not request.user.is_authenticated:
        print('not auth')
        return redirect('products')
    
    user = request.user
    order, created = Order.objects.get_or_create(user=user, complete=False)
    items = order.orderitem_set.all()
    
    context = {
        'items':items,
        'order':order,
        'num_cart_items':order.get_cart_items,
    }

    return render(request, 'cart.html', context)

def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    user = request.user
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(user=user, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('added', safe=False)

def checkout_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    num_cart_items = Order.objects.get(user=request.user, complete=False).get_cart_items
    print('number', num_cart_items)
    if num_cart_items == 0:
        return redirect('products')

    order = Order.objects.get(user=request.user, complete=False)
    items = order.orderitem_set.all()

    context = {
        'num_cart_items':num_cart_items,
        'items':items,
        'order':order,
        'form':ShippingAdressForm(),
    }

    return render(request, 'checkout.html', context)

def purchase_complete_view(request):
    if not request.user.is_authenticated:
        return redirect('products')

    context = {}
    order, created = Order.objects.get_or_create(user=request.user, complete=False)
    context['num_cart_items'] = order.get_cart_items

    order.complete = True
    order.save()

    return render(request, 'purchase_complete.html', context)