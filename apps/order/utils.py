from ast import expr_context
from .models import Order
from rest_framework import serializers

def delete_order(order):
    for o in order.orderproductsthroughtable_set.all():
        o.product.stock += o.quantity
        o.product.save(update_field=["stock",])
    order.delete()


def create_order(products, user):
    order = None
    oos_item = None
    try:
        order_price = 0
        order = Order.objects.create(
            customer=user,
            price=order_price
        )
        for product in products:
            item = product.get("item")
            quantity = product.get("quantity")
            if item.stock < quantity:
                oos_item = item
                break;
            order_price += (item.price * quantity)
            order.products.add(item, through_defaults={"quantity": quantity})
        order.price = order_price
        order.save(update_fields=["price",])
    except Exception as e:
        if oos_item:
            if order:
                delete_order(order=order)
            raise serializers.ValidationError(f"Item {oos_item.name} has been out of stock")
        if order:
            delete_order(order=order)
        raise 

    return order
