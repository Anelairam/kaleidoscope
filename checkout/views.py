from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your shoppings cart is empty at the moment')
        return redirect(reverse('portfolio'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LjJhEB6bQSdJesEAKEX1H9oEyn14weYCjCme4lZrZlldN6tWMC5tdMe16fZSCsJF5yokUVeE4iuOvs5bRhwKvz800Gw1ngFjV',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)