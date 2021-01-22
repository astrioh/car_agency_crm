from rest_framework import serializers

from .models import Dealer


class DealerSerializer(serializers.ModelSerializer):
    dealer_type_name = serializers.CharField(source='dealer_type.name', read_only=True)
    
    class Meta:
        model = Dealer
        fields = ['id', 'name', 'dealer_type_name', 'dealer_type', 'image', 'contact', 'address',
            'phone', 'email']