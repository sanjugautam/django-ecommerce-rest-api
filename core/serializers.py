from rest_framework.serializers import ModelSerializer

from core.models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        verbose_name = 'Customer Create/Fetch'


