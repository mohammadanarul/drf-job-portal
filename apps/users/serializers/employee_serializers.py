from django.contrib.auth.password_validation import validate_password
from django.utils.crypto import get_random_string
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.users.models import Employee, Recruiter, User


class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=Employee.objects.all())]
    )
    phone_number = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=Employee.objects.all())]
    )

    class Meta:
        model = Employee
        fields = (
            "pk",
            "full_name",
            "phone_number",
            "email",
            "is_active",
        )


class EmployeeRegisterSerializer(EmployeeSerializer):
    password1 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta(EmployeeSerializer.Meta):
        fields = EmployeeSerializer.Meta.fields + ("password1", "password2")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password1 = validated_data["password1"]
        password2 = validated_data["password2"]

        if password1 != password2:
            raise serializers.ValidationError({"password": "Password didn't match."})

        user = Employee(
            full_name=validated_data["full_name"],
            phone_number=validated_data["phone_number"],
            email=validated_data["email"],
            is_active=validated_data["is_active"],
            otp=get_random_string(6).upper(),
        )
        user.set_password(password1)
        user.save()
        return user
