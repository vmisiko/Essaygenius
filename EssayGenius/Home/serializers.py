from rest_framework import serializers
from .models import Orders, VueOrders, UploadFiles

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('name', 'description', 'currency',
            'amount', 'created_at', 'updated_at'
        )

class VueOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = VueOrders
        fields =" __all__"

class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFiles
        fields = "__all__"