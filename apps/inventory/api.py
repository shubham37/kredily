from base.viewsets import GenericViewSet as ViewSet

from rest_framework.mixins import ListModelMixin
from .models import Product
from .serializers import ProductSerializer
from base.api.pagination import SmallSetPagination


class ProductViewSet(ViewSet, ListModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = SmallSetPagination


