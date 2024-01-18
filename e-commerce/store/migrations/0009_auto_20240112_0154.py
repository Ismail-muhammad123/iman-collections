# Generated by Django 3.2.13 on 2024-01-12 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_store_tin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subscription_code', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.PositiveIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('canceled_at', models.DateTimeField(blank=True, null=True)),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptions', to='store.plan')),
            ],
        ),
        migrations.RemoveField(
            model_name='store',
            name='bio',
        ),
        migrations.CreateModel(
            name='SubscriptionPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[(0, 'Failed'), (1, 'Pending'), (2, 'Success')], max_length=3)),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscription_payments', to='store.store')),
                ('subscription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to='store.subscription')),
            ],
        ),
        migrations.AddField(
            model_name='subscription',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptions', to='store.store'),
        ),
    ]