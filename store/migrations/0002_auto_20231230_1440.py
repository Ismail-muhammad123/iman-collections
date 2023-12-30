# Generated by Django 3.2.13 on 2023-12-30 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='store',
            name='alternate_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='alternate_phone_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='bio',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='is_open',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='store',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='store',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='store',
            name='last_viewed',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='store',
            name='owener',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='store', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='store',
            name='rc_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='registration_certificate',
            field=models.FileField(null=True, upload_to='store_verification_files/'),
        ),
        migrations.DeleteModel(
            name='StoreVerification',
        ),
        migrations.DeleteModel(
            name='VerificationDocument',
        ),
    ]
