from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HardwareSerializer
from .models import Hardware


class HardwareViewSet(viewsets.ModelViewSet):
    queryset = Hardware.objects.all()
    serializer_class = HardwareSerializer

