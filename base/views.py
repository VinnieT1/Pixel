from django.shortcuts import render
from cart.models import Order
from users.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home_view(request):
    print('wtfffff22222')
    context = {}
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        context['num_cart_items'] = order.get_cart_items

    context['register_form'] = UserCreationForm()
    context['login_form'] = AuthenticationForm()

    return render(request, 'base.html', context)