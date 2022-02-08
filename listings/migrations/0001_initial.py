# Generated by Django 4.0.2 on 2022-02-08 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото 1')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото 2')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото 3')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото 4')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото 5')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото 6')),
                ('is_published', models.BooleanField(default=True, verbose_name='Статус публикации')),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
