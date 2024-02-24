# Generated by Django 4.0.10 on 2024-02-24 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_alter_city_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления записи')),
                ('base', models.CharField(max_length=255, verbose_name='Название валюты')),
                ('date', models.DateTimeField(verbose_name='Дата проверки валюты')),
            ],
            options={
                'verbose_name': 'Валюта',
            },
        ),
        migrations.CreateModel(
            name='CurrencyRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления записи')),
                ('currency_name', models.CharField(max_length=255, verbose_name='Валюта для сравнения')),
                ('rate', models.FloatField(verbose_name='Отношение валют')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='currency', to='geo.currency', verbose_name='Валюта')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]