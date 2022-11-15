from django.db import models

CATEGORY_CHOICES = [("other", "Разное"), ('unique', 'Уникальные'), ('priority', 'Приоритетные'),  ('basic', 'Базовые')]


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование Товара')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание Товара')
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES, verbose_name='Категория Товара')
    remainder = models.IntegerField(default=0, verbose_name='Остаток')
    price = models.PositiveIntegerField(max_length=9999999, default=0, verbose_name='Цена')

    def __str__(self):
        return f'{self.id}. {self.name}'