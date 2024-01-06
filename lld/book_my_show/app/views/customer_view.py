from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from ..exceptions.customer_exceptions import CustomerNotFoundException
from ..services.customer_service import CustomerService


class CustomerListView(APIView):
    """
    List all customers, or create a new customer.
    """

    def post(self, request, format=None):
        try:
            data = CustomerService.create_customer(request.data)
            return Response(data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerDetailView(APIView):
    """
    Retrieve, update or delete a customer instance.
    """

    def get(self, request, id, format=None):
        try:
            data = CustomerService.get_customer_by_id(id)
            return Response(data)
        except CustomerNotFoundException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
