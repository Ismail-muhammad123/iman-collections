# Generated by Django 3.2.13 on 2022-10-29 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='device',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]