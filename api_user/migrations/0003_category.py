# Generated by Django 3.2.9 on 2021-12-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'Categories',
            },
        ),
    ]