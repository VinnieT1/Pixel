import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from products.models import Product

# Create your views here.
def cart_view(request):
    if not request.user.is_authenticated:
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
    print(product_id, action)

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