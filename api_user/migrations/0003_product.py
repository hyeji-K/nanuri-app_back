# Generated by Django 3.2.9 on 2021-12-01 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(max_length=100)),
                ('link', models.URLField(null=True)),
                ('product_price', models.IntegerField()),
                ('total_ppl_cnt', models.IntegerField()),
                ('join_ppl_cnt', models.IntegerField(default=1, null=True)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('delivery_method', models.CharField(max_length=10)),
                ('detail_content', models.CharField(max_length=200, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='api_user.category')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='api_user.user')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]