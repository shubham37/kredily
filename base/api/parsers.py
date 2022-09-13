import json

from django.http import QueryDict
from rest_framework import parsers


class MultiPartJsonParser(parsers.MultiPartParser):
    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(stream, media_type=media_type, parser_context=parser_context)
        data = {}

        # For nested serializers, drf accepts values in dotted notation. E.g if location is nested serializer.
        # It will accept location.x and location.y if data is to be entered in form fields.
        # the 2 nested for loops, ensures that the JSON data sent in form field is converted to the above format.
        # e.g if the key is asset_location. and it has x and y keys inside. It will be converted to asset_location.x,
        # and asset_location.y

        for key, value in result.data.items():
            if type(value) != str:
                data[key] = value
                continue
            if "{" in value or "[" in value:
                try:
                    json_value = json.loads(value)
                    if type(json_value) == dict:
                        data[key] = value
                        for inner_key, inner_value in json_value.items():
                            data[f"{key}.{inner_key}"] = inner_value
                except ValueError:
                    data[key] = value
            else:
                data[key] = value

        qdict = QueryDict("", mutable=True)
        qdict.update(data)
        return parsers.DataAndFiles(qdict, result.files)
