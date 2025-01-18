from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HardwareSerializer
from .models import Hardware


class HardwareAPIList(generics.ListCreateAPIView):
    queryset = Hardware.objects.all()
    serializer_class = HardwareSerializer

class HardwareAPIUpdate(generics.UpdateAPIView):
    queryset = Hardware.objects.all()
    serializer_class = HardwareSerializer

class HardwareAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hardware.objects.all()
    serializer_class = HardwareSerializer

# class HardwareAPIView(APIView):
#     def get(self, request):
#         objects = Hardware.objects.all()
#         return Response({'posts': HardwareSerializer(objects, many=True).data})
    
#     def post(self, request):
#         serializer = HardwareSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT is not allowed.'})
#         try:
#             instance = Hardware.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exist.'})
        
#         serializer = HardwareSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'item': serializer.data})
        
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"ERROR": "Delete Method Is Not Allowed"})
        
#         # deleting an object from api

#         try:
#             instance = Hardware.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"ERROR": "Object not Found."})

#         return Response({"post": f"Object {str(pk)} is deleted"})
        
        

# class HardwareAPIView(generics.ListAPIView):
#     queryset = Hardware.objects.all()
#     serializer_class = HardwareSerializer
