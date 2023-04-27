from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from .forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register_user_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = UserCreationForm()

    return render(request, 'register_user.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('products')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')