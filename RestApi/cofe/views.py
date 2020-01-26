from .serializers import DrinkDetailSerializers, WorkerDetailSerializers, SaleSerializers
from .models import Drink, Worker, Sale
from .utils import ObjectViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework import viewsets


class DrinkViewSet(ObjectViewSet, viewsets.ModelViewSet):

    queryset = Drink.objects.all()
    serializer_class = DrinkDetailSerializers

    
class WorkerViewSet(ObjectViewSet, viewsets.ModelViewSet):
    
    queryset = Worker.objects.all()
    serializer_class = WorkerDetailSerializers


class SaleViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Worker.objects.all()
    serializer_class = SaleSerializers

    

  