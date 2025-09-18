from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().select_related('merchant','driver')
    serializer_class = OrderSerializer