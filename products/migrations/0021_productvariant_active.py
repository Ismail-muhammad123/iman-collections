# Generated by Django 3.2.13 on 2024-01-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20231230_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
