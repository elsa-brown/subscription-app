from rest_framework import serializers
from customers.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "first_name", 
            "last_name",
            "address_1",
            "address_2",
            "city",
            "state",
            "postal_code"
        ]

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "customer", 
            "plan_name",
            "price"
        ]