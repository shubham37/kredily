from rest_framework_nested import routers
from .api import OrderViewSet

default_router = routers.SimpleRouter()
default_router.register("orders", OrderViewSet, basename="order")
urlpatterns = default_router.urls

