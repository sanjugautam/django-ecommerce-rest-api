from rest_framework.serializers import ModelSerializer

from core.models import Customer


class CustomerSerializer(ModelSerializer):
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    class Meta:
        model = Customer
        fields = '__all__'


class CustomerViewSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'is_superuser', 'full_name', 'date_joined', 'location', 'email']


