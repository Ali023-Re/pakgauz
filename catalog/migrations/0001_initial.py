# Generated by Django 5.0.4 on 2024-05-08 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('contain', models.TextField()),
            ],
            options={
                'verbose_name': 'Торговая марка',
                'verbose_name_plural': 'Торговые марки',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Сategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('contain', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('contain', models.TextField()),
                ('packing', models.CharField(max_length=100)),
                ('count_in_box', models.IntegerField()),
                ('stock', models.BooleanField(default=True)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.brand')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.subcategory')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.сategory'),
        ),
    ]
