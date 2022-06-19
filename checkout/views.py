from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Currently, the cart is empty.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KzOoFDK1OXoo8Fox5qkVaLQ4mh3ChQ8liy0bS8DgddYiMqVnW3NBzYDut9hX0Ig2iKCofn2LSmZ4B7xrBN9NSY200qNugh8YT',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)