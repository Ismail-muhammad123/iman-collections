# Generated by Django 4.0.6 on 2022-10-03 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
    ]
