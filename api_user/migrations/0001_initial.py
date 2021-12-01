# Generated by Django 3.2.9 on 2021-12-01 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                ('user_bank', models.CharField(blank=True, max_length=32, null=True)),
                ('banknum', models.IntegerField(blank=True, null=True)),
                ('user_number', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('social_id', models.ForeignKey(db_column='social_id', on_delete=django.db.models.deletion.CASCADE, to='api_user.sociallogin')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
