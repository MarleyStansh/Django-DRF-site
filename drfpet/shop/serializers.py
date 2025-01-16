import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Hardware


# class HardwareModel:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description

class HardwareSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(default="")
    price = serializers.IntegerField(default=0)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    cat_id = serializers.IntegerField()
    num_in_stock = serializers.IntegerField(default=0)
    params = serializers.CharField(default="")

# def encode():
#     model = HardwareModel("Processor", "Powerful processor")
#     model_sr = HardwareSerializer(model)
#     print(model_sr.data, type(model_sr), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"title": "Processor", "description": "Powerful processor"}')
#     data = JSONParser().parse(stream)
#     serializer = HardwareSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)