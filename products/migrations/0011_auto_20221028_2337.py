# Generated by Django 3.2.13 on 2022-10-28 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0010_remove_color_added_by_delete_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='added_by',
            field=models.ForeignKey(limit_choices_to={'staff': True}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='categories_added', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_by',
            field=models.ForeignKey(limit_choices_to={'staff': True}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products_added', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='size',
            name='added_by',
            field=models.ForeignKey(limit_choices_to={'staff': True}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sizes_added', to=settings.AUTH_USER_MODEL),
        ),
    ]
