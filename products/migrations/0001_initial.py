# Generated by Django 3.2.7 on 2021-10-18 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('T', 'Tailor'), ('S', 'Seller')], max_length=5)),
                ('total_earnings', models.FloatField()),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('category', models.CharField(choices=[('TD', 'Tailored'), ('SH', 'Shoes'), ('ST', 'Shirts'), ('CP', 'Caps'), ('TR', 'trousers'), ('OTH', 'Others')], max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('delivery_days', models.DurationField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('suplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.suplier')),
            ],
        ),
    ]
