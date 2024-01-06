from ..exceptions.customer_exceptions import CustomerNotFoundException
from ..models.customer import Customer
from ..serializers.customer_serializer import CustomerSerializer
from ..exceptions.serializer_exceptions import SerializerException
from rest_framework import serializers


class CustomerService:
    @staticmethod
    def get_object(id):
        try:
            return Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            raise CustomerNotFoundException(
                id=id, additional_info={"reason": "Customer not found"}
            )

    @staticmethod
    def get_customer_by_id(id):
        customer = CustomerService.get_object(id)
        serializer = CustomerSerializer(customer)
        return serializer.data

    @staticmethod
    def create_customer(data):
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            print("######################" * 20)
            print(serializer)
            serializer.save()
            return serializer.data
        else:
            raise serializers.ValidationError(serializer.errors)
