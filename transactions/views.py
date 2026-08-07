from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BulkTransactionSerializer
from .models import Account, Transaction
from django.db import transaction

class BulkTransactionView(APIView):
    def post(self, request):
        # validate incoming data
        serializer = BulkTransactionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
        
        validated_data = serializer.validated_data
        transactions_to_create = []
        accounts_created = 0

        with transaction.atomic():
            # loop through the accounts 
            for account_data in validated_data["accounts"]:
                transactions = account_data.pop("transactions")# separate transactions rom accounts first

                account = Account.objects.create(**account_data)
                accounts_created += 1

                for transaction_data in transactions:
                    transactions_to_create.append(Transaction( 
                        account_id=account,
                        **transaction_data)
                        
                    )
            
            Transaction.objects.bulk_create(transactions_to_create)
        return Response(
            {
                "message": "Bulk transactions created successfully.",
                "accounts_created": accounts_created,
                "transactions_created": len(transactions_to_create),
            },
            status=status.HTTP_201_CREATED,
        )





