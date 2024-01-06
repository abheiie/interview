from rest_framework import serializers

from ..models.customer import Customer
from ..models.user import User
from ..serializers.user_serializer import UserSerializer


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        # fields = ["id", "full_name", "city", "phone", "email"]
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)
        customer = Customer.objects.create(user=user, **validated_data)
        return customer


# def unique_field_validator(value):
#     if YourModel.objects.filter(your_field=value).exists():
#         raise ValidationError("This value must be unique.")


# class YourModelSerializer(serializers.ModelSerializer):
#     your_field = serializers.CharField(validators=[unique_field_validator])

#     class Meta:
#         model = YourModel
#         fields = "__all__"


# # serializers.py
# from rest_framework import serializers
# from .models import Customer


# class CustomerSerializer(serializers.ModelSerializer):
#     create_only_full_name = serializers.BooleanField(write_only=True, required=False)

#     class Meta:
#         model = Customer
#         fields = ["full_name", "city", "phone", "email", "create_only_full_name"]

#     def validate(self, data):
#         create_only_full_name = data.get("create_only_full_name", False)

#         # If create_only_full_name is True, ensure only full_name is provided
#         if create_only_full_name:
#             if "full_name" in data and len(data) > 1:
#                 raise serializers.ValidationError(
#                     "When create_only_full_name is True, only full_name should be provided."
#                 )
#             if "full_name" not in data:
#                 raise serializers.ValidationError(
#                     "full_name is required when create_only_full_name is True."
#                 )

#         return data

#     def create(self, validated_data):
#         create_only_full_name = validated_data.pop("create_only_full_name", False)

#         # If create_only_full_name is True, create a customer with only full_name
#         if create_only_full_name:
#             return Customer.objects.create(full_name=validated_data["full_name"])

#         return Customer.objects.create(**validated_data)
