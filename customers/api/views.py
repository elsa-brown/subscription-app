from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from customers.models import Customer
from .serializers import CustomerSerializer, SubscriptionSerializer

class CustomerApiView(APIView):
    def get(self, request):
        return Response("Add customer data in JSON format below, and click POST to add to database.")
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(APIView):
    def get_object(self, customer_id):
        # helper method
        try:
            return Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return None

    def get(self, request, customer_id):
        customer = self.get_object(customer_id)
        if not customer:
            return Response(
                {"Customer does not exist. Please try again."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        if not customer:
            return Response(
                {"Customer does not exist. Please try again."},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'customer': customer,
            'plan_name': request.data.get('plan_name'),
            'price': request.data.get('price')
        }

        serializer = SubscriptionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)