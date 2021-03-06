from rest_framework import viewsets

from .serializers import TransactionSerializer
from .models import Transaction


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("trans_date")
    serializer_class = TransactionSerializer
