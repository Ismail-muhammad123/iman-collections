# Generated by Django 3.2.7 on 2021-10-19 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_rename_size_cart_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='quentity',
            new_name='quantity',
        ),
    ]
