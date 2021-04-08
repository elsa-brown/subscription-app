from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from customers.models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(APIView):
    def post(self, request):
        # data = {
        #     'first_name': request.data.get('first_name'),
        #     'last_name': request.data.get('last_name'),
        #     'address_1': request.data.get('address_1'),
        #     'address_2': request.data.get('address_2'),
        #     'last_name': request.data.get('last_name'),
        #     'last_name': request.data.get('last_name'),
        # }
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
