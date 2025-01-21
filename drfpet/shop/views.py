from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import HardwareSerializer
from .models import Hardware, Category
from .permissions import IsAdminOrReadOnly


class HardwareViewSet(viewsets.ModelViewSet):
    serializer_class = HardwareSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Hardware.objects.all()
        return Hardware.objects.filter(pk=pk)

    permission_classes = (IsAdminOrReadOnly, )

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': [cats.name]})
