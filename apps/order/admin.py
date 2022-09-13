from django.contrib import admin
from .models import Order, OrderProductsThroughTable

class OrderProductsThroughTableInline(admin.TabularInline):
    model = OrderProductsThroughTable
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderProductsThroughTableInline,)
    search_fields = ("id","customer__id")
    list_display = ("id", "customer", "price")
    ordering = ("-created_at",)
