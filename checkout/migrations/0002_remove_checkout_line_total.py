# Generated by Django 2.2.5 on 2019-10-21 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='line_total',
        ),
    ]