# Generated by Django 3.2.13 on 2022-10-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_merge_0015_merge_20221029_0037_0016_cart_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
