# Generated by Django 3.2.9 on 2021-12-27 23:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='join_ppl_cnt',
            field=models.IntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_ppl_cnt',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_bank',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
    ]
