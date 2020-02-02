from rest_framework import serializers
from app.models import Customer, Account, Action


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        exclude = ['user']
        
        

class AccountSerializer(serializers.ModelSerializer):
    
    actions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('balance', 'actions')
        read_only_fields = ('balance', 'actions')


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = ('account', 'amount', 'date')
        read_only_fields = ('date',)


