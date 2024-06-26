# Generated by Django 3.2.13 on 2023-12-30 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0019_product_on_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('color_hex_code', models.CharField(max_length=20)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='available_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_size',
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='store.store'),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='sub_categories/')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.CharField(blank=True, default='', max_length=200, unique=True)),
                ('added_by', models.ForeignKey(limit_choices_to={'staff': True}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sub_categories_added', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_categories', to='products.category')),
            ],
            options={
                'verbose_name_plural': 'sub categories',
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available_quantity', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='product_images/')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_variants', to='products.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variants', to='products.product')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_variants', to='products.size')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product_variant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productvariant'),
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(related_name='products', to='products.ProductImage'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.subcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='variants',
            field=models.ManyToManyField(related_name='products', to='products.ProductVariant'),
        ),
    ]
