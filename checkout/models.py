from django.db import models
from cart.models import Cart
from django.contrib.auth.models import User


ORDER_STATUS = (
    ('opened', 'opened'),
    ('dispatched', 'dispatched'),
    ('closed', 'closed')
)


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    discount_total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    grand_total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=ORDER_STATUS, default='opened')
    order_id = models.CharField(max_length=20, default='00000001', unique=True)
    full_name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=30, blank=False)
    postcode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=30, blank=False)
    address1 = models.CharField(max_length=50, blank=False)
    address2 = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=30, blank=False)

    def __unicode__(self):
        return self.order_id
