# Generated by Django 3.2.13 on 2024-01-14 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20240114_0007'),
        ('order', '0009_auto_20240106_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_fee',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='order',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='tracking_id',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='delivery_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='delivery_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='delivery_status',
            field=models.PositiveIntegerField(choices=[(1, 'Unfulfiled'), (2, 'Fulfiled')], default=1),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='store.store'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='tracking_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
