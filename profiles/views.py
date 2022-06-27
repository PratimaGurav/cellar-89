from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, FavoriteItem
from .forms import UserProfileForm

from products.models import Product
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    try:
        favorites = FavoriteItem.objects.filter(user=request.user.id)[0]
    except IndexError:
        favorites_items = None
    else:
        favorites_items = favorites.product.all()

    if not favorites_items:
        messages.info(request, 'There are no bottles in your favorites yet.')        

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'favorites_items': favorites_items,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def add_to_favorites(request, product_id):
    """
    Adds the product to the users Favorites.
    """
    product = get_object_or_404(Product, pk=product_id)
    try:
        favoritesitem = get_object_or_404(FavoriteItem, user=request.user.id)

    except Http404:
        favoritesitem = FavoriteItem.objects.create(user=request.user)
    if product in favoritesitem.product.all():
        messages.info(request, 'Your Favorites contains this product already,')
    else:
        favoritesitem.product.add(product)
        messages.info(
            request, f'Added {product.name[:30]}.. to your Favorites.'
        )
    return redirect(reverse('product_detail', args=[product_id]))


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)