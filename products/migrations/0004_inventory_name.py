# Generated by Django 4.0.6 on 2022-10-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
