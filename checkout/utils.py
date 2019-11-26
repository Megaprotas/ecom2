import string
import random
from .models import Checkout


def generate_id(length=5, chars=string.ascii_lowercase + string.digits):
    cartid = "".join(random.choice(chars) for i in range(length))
    try:
        order_id = Checkout.objects.get(order_id=cartid)
        generate_id()
    except Checkout.DoesNotExist:
        return cartid