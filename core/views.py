from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from core.models import Customer
from core.serializers import CustomerSerializer, CustomerViewSerializer


class CustomerList(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerViewSerializer


class CustomerCreate(CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
