# Generated by Django 3.2.13 on 2024-01-06 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20240104_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='delivery_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]