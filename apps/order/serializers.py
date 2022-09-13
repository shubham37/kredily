from apps.inventory.models import Product
from apps.inventory.serializers import ProductSerializer
from .models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ("id", "price", "customer", "products")
    
    def get_products(self, obj):
        products = []
        for item in obj.orderproductsthroughtable_set.all():
            data = ProductSerializer(item.product).data
            data["quantity"] = item.quantity

            products.append(data)
        return products

class MultipleProductsSerializer(serializers.Serializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), required=True)
    quantity = serializers.IntegerField(default=1, required=False)


class CreateOrderSerializer(serializers.Serializer):
    products = MultipleProductsSerializer(many=True)

