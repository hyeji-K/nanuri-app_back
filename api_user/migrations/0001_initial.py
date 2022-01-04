# Generated by Django 3.2.9 on 2021-12-31 16:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='SocialLogin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('social_id', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'db_table': 'SocialLogin',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('user_area', models.CharField(max_length=128)),
                ('user_nick', models.CharField(max_length=128, unique=True)),
                ('score', models.IntegerField(default=0, null=True)),
                ('user_bank', models.CharField(blank=True, default='', max_length=32)),
                ('banknum', models.IntegerField(blank=True, default=0)),
                ('user_number', models.IntegerField(blank=True, default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('social_id', models.ForeignKey(db_column='social_id', on_delete=django.db.models.deletion.CASCADE, to='api_user.sociallogin')),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(max_length=100)),
                ('link', models.URLField(max_length=1000, null=True)),
                ('productImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_price', models.IntegerField()),
                ('total_ppl_cnt', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('join_ppl_cnt', models.IntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('delivery_method', models.CharField(max_length=10)),
                ('detail_content', models.TextField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api_user.category')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api_user.user')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('credit_method', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_user.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='api_user.user')),
            ],
            options={
                'db_table': 'Order',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_user.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_user.user')),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
    ]
