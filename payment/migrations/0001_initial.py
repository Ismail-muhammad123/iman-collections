# Generated by Django 3.2.8 on 2021-11-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('currency', models.CharField(max_length=3, null=True)),
                ('channel', models.CharField(max_length=10, null=True)),
                ('card_type', models.CharField(max_length=10, null=True)),
                ('bank', models.CharField(max_length=30, null=True)),
                ('card_last_four', models.CharField(max_length=4, null=True)),
                ('county_code', models.CharField(max_length=3, null=True)),
                ('account_name', models.CharField(max_length=100, null=True)),
                ('refrence_code', models.CharField(max_length=200)),
                ('status', models.IntegerField(choices=[(1, 'SUCCESS'), (0, 'FAILED')], null=True)),
            ],
        ),
    ]
