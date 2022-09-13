from rest_framework_nested import routers
from .api import ProductViewSet

default_router = routers.SimpleRouter()
default_router.register("products", ProductViewSet, basename="product")
urlpatterns = default_router.urls

