# Generated by Django 3.2.7 on 2021-10-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211019_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='suplier',
        ),
        migrations.AddField(
            model_name='product',
            name='brand_name',
            field=models.CharField(default='chitex', max_length=250),
            preserve_default=False,
        ),
    ]
