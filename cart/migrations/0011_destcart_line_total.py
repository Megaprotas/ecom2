# Generated by Django 2.2.5 on 2019-11-08 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_remove_destcart_line_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='destcart',
            name='line_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
