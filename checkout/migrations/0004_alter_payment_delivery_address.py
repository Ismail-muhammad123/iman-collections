# Generated by Django 4.0.6 on 2022-08-25 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_payment_country_payment_first_name_payment_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='delivery_address',
            field=models.TextField(),
        ),
    ]