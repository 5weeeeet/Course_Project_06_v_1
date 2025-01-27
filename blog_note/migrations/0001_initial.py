# Generated by Django 4.2.5 on 2023-10-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=100, null=True, verbose_name='slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('sign_of_publication', models.BooleanField(default=True, verbose_name='Признак публикации')),
                ('quantity_views', models.IntegerField(default=0, verbose_name='Счетчик просмотров')),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'записи',
            },
        ),
    ]
