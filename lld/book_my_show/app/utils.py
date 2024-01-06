from django.core.serializers import serialize
import json


def jsonify(model_object):
    serialized_data = serialize("json", [model_object])
    deserialized_data = json.loads(serialized_data)
    return deserialized_data
