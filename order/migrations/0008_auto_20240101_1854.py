# Generated by Django 3.2.13 on 2024-01-01 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_productvariant_active'),
        ('store', '0004_auto_20240101_1854'),
        ('order', '0007_auto_20221029_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_status',
            field=models.PositiveIntegerField(choices=[(1, 'Unfulfiled'), (2, 'Fulfiled')], default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='store.store'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='products.productvariant'),
        ),
    ]
