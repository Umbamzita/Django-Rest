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

    def create(self, validated_data):
        #create action and sum (balance and amount)
        if validated_data['account'].balance + validated_data['amount'] > 0:
            validated_data['account'].balance += validated_data['amount']
            validated_data['account'].save()
        else:
            raise serializers.ValidationError(('Not enough money'))

        return Action.objects.create(**validated_data)


