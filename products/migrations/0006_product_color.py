# Generated by Django 3.2.8 on 2021-10-22 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20211019_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='white', max_length=200),
            preserve_default=False,
        ),
    ]
