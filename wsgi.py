from base.services import _set_django_settings_module
from django.core.wsgi import get_wsgi_application

_set_django_settings_module()

application = get_wsgi_application()
