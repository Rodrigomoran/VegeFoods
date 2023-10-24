from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['nombre ', 'precio', 'categoria', 'fecha']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
