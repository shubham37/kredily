from base.viewsets import GenericViewSet as ViewSet

from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Order
from .serializers import OrderSerializer, CreateOrderSerializer
from base import response
from .utils import create_order

class OrderViewSet(ViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data.get("products")
        order = create_order(products=data, user = self.request.user)
        if order:
            return response.Created({"id": str(order.id)})
        else:
            return response.BadRequest("Try Again")

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "create":
            return CreateOrderSerializer
        return self.serializer_class
