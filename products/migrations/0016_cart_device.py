# Generated by Django 3.2.13 on 2022-10-29 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='device',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
