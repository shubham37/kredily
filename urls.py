from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Kredily API",
        default_version="1.0.1",
        description="Guide to use Kredily API",
        url="http://localhost:8000",
    ),
    public=True,
    authentication_classes=(),
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.customer.urls")),
    path("api/", include("apps.order.urls")),
    path("api/", include("apps.inventory.urls")),
    path("api-doc/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
