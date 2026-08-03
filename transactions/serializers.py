from .models import Account, Transaction
from rest_framework import serializers

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'reference',
            'amount',
            'transaction_type',
            'description'

        )
class AccountSerializer(serializers.ModelSerializer):

    transactions = TransactionSerializer(many=True)
    class Meta:
       
 
        model = Account
        fields = [
            'name',
            'account_number',
            'transactions',
        ]

class BulkTransactionSerilizer(serializers.Serializer):
    accounts = AccountSerializer(many=True)