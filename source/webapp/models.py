from django.db import models

CATEGORY_CHOICES = [("other", "Разное"), ('unique', 'Уникальные'), ('priority', 'Приоритетные'),  ('basic', 'Базовые')]


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование Товара')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание Товара')
    category = models.TextField(max_length=25, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES, verbose_name='Категория')
    remainder = models.IntegerField(max_length=50, verbose_name='Остаток')
    price = models.IntegerField(max_length=8, verbose_name='Стоимость')

    def __str__(self):
        return f'{self.id}. {self.name}'