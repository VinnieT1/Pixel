from django.shortcuts import render

# Create your views here.
def register_user_view(request):
    return render(request, 'base.html')

def login_view(request):
    return render(request, 'base.html')

def logout_view(request):
    return render(request, 'base.html')