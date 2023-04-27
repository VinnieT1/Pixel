from django.shortcuts import redirect

# Create your views here.
def home_view(request):
    return redirect('products')