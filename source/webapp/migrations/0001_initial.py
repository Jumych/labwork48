# Generated by Django 4.1.3 on 2022-11-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование Товара')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание Товара')),
                ('category', models.TextField(choices=[('unique', 'Уникальные'), ('priority', 'Приоритетные'), ('basic', 'Базовые')], default=[('unique', 'Уникальные'), ('priority', 'Приоритетные'), ('basic', 'Базовые')], max_length=25, verbose_name='Категория')),
                ('remainder', models.IntegerField(max_length=50, verbose_name='Остаток')),
                ('price', models.IntegerField(max_length=8, verbose_name='Стоимость')),
            ],
        ),
    ]
