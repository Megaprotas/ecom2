import time
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Checkout
from .utils import generate_id


@login_required
def checkout(request):
    try:
        idcart = request.session['cart_id']
        cart = Cart.objects.get(id=idcart)
    except:
        idcart = None
        return redirect(reverse('cart'))

    try:
        checkout_form = Checkout.objects.get(cart=cart)
    except Checkout.DoesNotExist:
        checkout_form = Checkout(cart=cart)
        checkout_form.user = request.user
        checkout_form.order_id = generate_id()
        checkout_form.save()
    except:
        return redirect(reverse('cart'))

    if checkout_form.status == 'closed':
        del request.session['cart_id']
        del request.session['dest_total']
        return redirect(reverse('cart'))

    context = {}
    return render(request, 'checkout.html', context)
