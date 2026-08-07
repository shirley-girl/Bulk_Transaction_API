from django.urls import path
from .views import BulkTransactionView
urlpatterns = [
    path('transactions/bulk',BulkTransactionView.as_view(), name="bulk_transaction")
]