# Generated by Django 2.0 on 2018-01-27 09:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(default='', max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('house_no', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('pin', models.IntegerField(default=328001, validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(100000)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='all_orders_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0.0)),
                ('paying_amount', models.IntegerField(default=0)),
                ('order_date', models.DateField()),
                ('order_delievered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=500)),
                ('product_image', models.FileField(upload_to='')),
                ('product_type', models.CharField(default='', max_length=500)),
                ('small_description', models.CharField(default='', max_length=340)),
                ('price', models.FloatField()),
                ('base_quantity', models.IntegerField()),
                ('synonyms', models.TextField(default=' ', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='product_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='shopping_cart_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('amount_to_pay', models.IntegerField(default=0)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='all_orders_table',
            name='ordered_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='all_orders_table',
            name='user_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
