# Generated by Django 3.2.8 on 2021-10-26 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_category_product_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sizes',
            new_name='size',
        ),
    ]
