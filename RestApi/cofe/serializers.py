from rest_framework import serializers
from.models import *
from django.db.models import Sum, Count

class DrinkDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = Drink
        fields ="__all__"


class WorkerDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = Worker
        exclude = ['drinks']


class SaleSerializers(serializers.ModelSerializer):

    total = serializers.SerializerMethodField()  

    class Meta:
        model = Worker
        fields = ('first_name','last_name', 'total')

    def get_total(self, obj):
        qs1 = obj.__class__.objects.filter(id=obj.id).aggregate(total_sum = Sum('drinks__price'))
        qs2 = obj.__class__.objects.filter(id=obj.id).aggregate(count = Count('drinks'))
        return qs1, qs2

