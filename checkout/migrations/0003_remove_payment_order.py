# Generated by Django 3.2.13 on 2024-01-14 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_payment_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='order',
        ),
    ]
