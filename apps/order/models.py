from itertools import product
from django.db import models
from base.models import TimeStampedUUIDModel
from apps.inventory.models import Product
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model

class Order(TimeStampedUUIDModel):
    customer = models.ForeignKey(get_user_model(), verbose_name=_("Customer"), related_name="orders", on_delete=models.CASCADE)
    products = models.ManyToManyField(
        Product,
        through="OrderProductsThroughTable",
        through_fields=(
            "order",
            "product",
        ),
        related_name="orders",
        verbose_name=_("Product"),        
    )
    price = models.FloatField(_("Order Price"))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        db_table = "orders"

    def __str__(self):
        return f"{self.id}"


class OrderProductsThroughTable(TimeStampedUUIDModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product"),
    )
    order = models.ForeignKey(
        "Order",
        on_delete=models.CASCADE,
        verbose_name=_("Order"),
    )

    quantity = models.BigIntegerField(_("Quantity of an item"))

    def __str__(self):
        return f"{self.product} - {self.order}"

