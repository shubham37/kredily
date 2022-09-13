import os


def _set_django_settings_module():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")
