from django.shortcuts import render

# Create your views here.
def product_view(request, pk):
    return render(request, 'product.html', {'pk':pk})

def all_products_view(request):
    return render(request, 'home.html')

def products_type_view(request, product_type):
    return render(request, 'base.html', {'product_type':product_type})

def register_product_view(request):
    return render(request, 'base.html', {'pk':'register prod', 'product_type':'prod_type'})

def delete_product_view(request):
    pass