from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Destination(models.Model):
    AFRICA = 'africa'
    ASIA = 'asia'
    EUROPE = 'europe'
    AMERICAS = 'americas'
    OCEANIA = 'oceania'
    CONTINENT = (
        (AFRICA, 'africa'),
        (ASIA, 'asia'),
        (EUROPE, 'europe'),
        (AMERICAS, 'americas'),
        (OCEANIA, 'oceania')
    )

    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='upload_pics')
    continent = models.CharField(max_length=20, choices=CONTINENT, default=EUROPE, blank=True, null=True)
    active = models.BooleanField(default=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('destination', kwargs={'pk': self.pk})