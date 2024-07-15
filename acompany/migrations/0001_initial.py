# Generated by Django 5.0.7 on 2024-07-15 21:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fantasyName', models.CharField(blank=True, max_length=100)),
                ('cnpj', models.CharField(blank=True, max_length=100, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('contact', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
