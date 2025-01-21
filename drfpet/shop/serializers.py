import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Hardware


class HardwareSerializer(serializers.ModelSerializer):
    class Meta:
        user = serializers.HiddenField(default=serializers.CurrentUserDefault())
        model = Hardware
        fields = ("title", "params", "cat", "price", "num_in_stock")
