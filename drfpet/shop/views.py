from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HardwareSerializer
from .models import Hardware


class HardwareAPIView(APIView):
    def get(self, request):
        lst = Hardware.objects.all().values()
        return Response({'posts': lst})
    
    def post(self, request):
        post_new = Hardware.objects.create(
            title=request.data['title'],
            cat_id = request.data['cat_id'],
        )
        post_new.save()
        return Response({'post': 123})

# class HardwareAPIView(generics.ListAPIView):
#     queryset = Hardware.objects.all()
#     serializer_class = HardwareSerializer
