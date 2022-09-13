from base.services import _set_django_settings_module
from django.core.asgi import get_asgi_application

_set_django_settings_module()

application = get_asgi_application()
