from django.shortcuts import render, get_object_or_404, reverse, redirect
from core.models import Destination
from .models import Cart, DestCart


def cart(request):
    try:
        idcart = request.session['cart_id']
        cart = Cart.objects.get(id=idcart)
    except:
        idcart = None
        return redirect(reverse('index'))

    if idcart:
        grand_total = 0.00
        total_before_discount = 0.00
        you_save = 0.00
        for item in cart.destcart_set.all():
            actual_price = float(item.destination.price) - float(item.destination.discount_price)
            line_total = float(actual_price) * item.quantity
            line_total2 = float(item.destination.price) * item.quantity
            grand_total += line_total
            total_before_discount += line_total2
            you_save = total_before_discount - grand_total
        request.session['dest_total'] = cart.destcart_set.count()
        cart.total_before_discount = total_before_discount
        cart.total = grand_total
        cart.you_save = you_save
        cart.save()
        context = {'cart': cart}
    else:
        context = {'empty': True}
    return render(request, 'cart.html', context)


def edit_cart(request, id):
    request.session.set_expiry(5000)
    try:
        qty = request.GET.get('qty')
        updated_qty = True
    except:
        qty = None
        updated_qty = False

    try:
        idcart = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        idcart = new_cart.id

    cart = Cart.objects.get(id=idcart)

    try:
        destination = Destination.objects.get(id=id)
    except Destination.DoesNotExist:
        print('does not exist')
        # message about non existent item return to index

    cart_item, created = DestCart.objects.get_or_create(cart=cart, destination=destination)
    if created:
        pass
    # message telling about creation

    if updated_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()
    else:
        pass
    return redirect(reverse('cart'))
