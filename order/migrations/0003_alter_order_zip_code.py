# Generated by Django 4.0.6 on 2022-10-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_product_remove_order_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
