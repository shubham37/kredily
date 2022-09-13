from django.db import models
from base.models import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _

class Product(TimeStampedUUIDModel):
    name = models.CharField(_("Product Name"), max_length=256)
    price = models.FloatField(_("Product Price"))
    stock = models.BigIntegerField(_("Available Stock"))

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        db_table = "products"

    def __str__(self):
        return f"{self.id} - {self.name}"

