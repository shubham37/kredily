from enum import IntEnum

import requests
from django.conf import settings
from requests.adapters import HTTPAdapter, Retry

build_mode = settings.BUILD_MODE
if build_mode in ["LOCAL"]:
    parent_dir = ""
else:
    parent_dir = build_mode.lower() + "/"


class ChoiceMixin(IntEnum):
    """
    Inherit this class in the types of choice for choices attribute in models.IntegerField
    """

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]



def get_base_path():
    if build_mode in ["LOCAL"]:
        base_path = settings.MEDIA_ROOT
    else:
        base_path = build_mode.lower()
    return base_path

