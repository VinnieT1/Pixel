from django.shortcuts import render

# Create your views here.
def product_view(request, pk):
    return render(request, 'base.html', {'pk':pk})

def all_products_view(request):
    return render(request, 'base.html')

def products_type_view(request, product_type):
    return render(request, 'base.html', {'product_type':product_type})

def register_product_view(request):
    pass

def delete_product_view(request):
    pass