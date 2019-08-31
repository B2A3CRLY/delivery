from rest_framework import generics, views, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from backend.models import Delivery, Client, Parcel
from .serializers import DeliverySerializer


class DeliveryList(generics.ListAPIView):
    serializer_class = DeliverySerializer
    def get_queryset(self):
        user = self.request.user
        queryset = Delivery.objects.filter(created_by = user)
        if user.is_superuser:
            queryset = Delivery.objects.all().order_by("-id")
        return queryset


class DeliveryCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    """def create(self, request):
        try:
            parcel = get_object_or_404(
                Parcel,
                tracking_number=request.data.get("parcel")["tracking_number"])
            if parcel:
                pass
            else:
                parcel = None
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(parcel=parcel)
            headers = self.get_success_headers(serializer.data)
            response = Response(serializer.data,
                                status=status.HTTP_201_CREATED,
                                headers=headers,
                                )
        except Exception as e:
            print("Error ", e)
            print("Error data ", request.data)
            response = JsonResponse(
                {"error": "Une erreur inatendue s'est produite"})

        return response"""


class DeliveryRetrieve(generics.RetrieveAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class DeliveryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated, )
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def delivery_detail(request, pk):
    try:
        delivery = Delivery.objects.get(pk=pk)
    except Delivery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DeliverySerializer(delivery, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            parcels = request.data.pop("parcels")
            for parcel in parcels:
                delivery.parcels.add(parcel.get("id"))
            serializer = DeliverySerializer(delivery, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Exception as e:
            print("Erreur :", e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'POST':
        parcels = request.data.pop("parcels")
        for parcel in parcels:
            delivery.parcels.remove(parcel.get("id"))
        return Response(status=status.HTTP_204_NO_CONTENT)
    """elif request.method == 'DELETE':
        delivery.delete()"""
    
        