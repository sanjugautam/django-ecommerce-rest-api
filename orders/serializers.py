from rest_framework.serializers import ModelSerializer

from orders.models import Orders


class OrderSerializer(ModelSerializer):
    def create(self, validated_data):
        new_order = Orders()
        new_order.buyer = validated_data["buyer"]
        new_order.status = validated_data["status"]
        new_order.order_price = validated_data["order_price"]
        new_order.shipping_address = validated_data["shipping_address"]
        new_order.save()
        new_order.order_items.set(validated_data["order_items"])
        new_order.save()
        return new_order

    class Meta:
        model = Orders
        fields = '__all__'
