from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from orders.models import Orders
from orders.serializers import OrderSerializer


class OrderListAPIView(ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer


class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
