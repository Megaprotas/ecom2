from django.db import models
from core.models import Destination


class Cart(models.Model):
    total_before_discount = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    grand_total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    you_save = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "Your cart ID is %s" %(self.id)


class DestCart(models.Model):
    cart = models.ForeignKey(Cart,  on_delete=models.CASCADE, blank=True, null=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __unicode__(self):
        try:
            return str(self.cart.id)
        except:
            return self.destination.name