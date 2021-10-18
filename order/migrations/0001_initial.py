# Generated by Django 3.2.7 on 2021-10-18 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('quentity', models.IntegerField()),
                ('total_amount', models.FloatField()),
                ('delivery_date', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.suplier')),
                ('tailor_reciever', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tailor', to='products.suplier')),
            ],
        ),
    ]
