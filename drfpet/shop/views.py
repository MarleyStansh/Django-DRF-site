from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HardwareSerializer
from .models import Hardware


class HardwareAPIView(APIView):
    def get(self, request):
        objects = Hardware.objects.all()
        return Response({'posts': HardwareSerializer(objects, many=True).data})
    
    def post(self, request):
        serializer = HardwareSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item_new = Hardware.objects.create(
            title = request.data['title'],
            cat_id = request.data['cat_id'],
        )
        return Response({'post': HardwareSerializer(item_new).data})

# class HardwareAPIView(generics.ListAPIView):
#     queryset = Hardware.objects.all()
#     serializer_class = HardwareSerializer
