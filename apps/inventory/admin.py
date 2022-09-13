from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("id","name")
    list_display = ("id", "name", "price", "stock")
    ordering = ("-created_at",)
