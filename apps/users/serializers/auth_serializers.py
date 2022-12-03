from rest_framework import serializers
from apps.users.models import User


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("otp",)
