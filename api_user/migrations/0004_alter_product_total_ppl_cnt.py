# Generated by Django 3.2.9 on 2021-12-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='total_ppl_cnt',
            field=models.IntegerField(null=True),
        ),
    ]
