# Generated by Django 2.2.5 on 2019-10-21 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('discount_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('status', models.CharField(choices=[('opened', 'opened'), ('dispatched', 'dispatched'), ('closed', 'closed')], default='opened', max_length=50)),
                ('order_id', models.CharField(default='00000001', max_length=20, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=30)),
                ('postcode', models.CharField(blank=True, max_length=10)),
                ('city', models.CharField(max_length=30)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=30)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
