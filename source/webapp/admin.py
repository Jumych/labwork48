from django.contrib import admin
from webapp.models import Product


# Register your models here.
class Product_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'remainder', 'price']
    list_filter = ['category']
    search_fields = ['name']
    exclude = []

admin.site.register(Product)