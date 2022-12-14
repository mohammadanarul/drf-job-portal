from django.contrib.auth.password_validation import validate_password
from django.utils.crypto import get_random_string
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.users.models import Recruiter


class RecruiterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=Recruiter.objects.all())]
    )
    phone_number = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=Recruiter.objects.all())]
    )

    class Meta:
        model = Recruiter
        fields = (
            "id",
            "full_name",
            "phone_number",
            "email",
            "is_active",
        )


class RecruiterRegisterSerializer(RecruiterSerializer):
    password1 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta(RecruiterSerializer.Meta):
        fields = RecruiterSerializer.Meta.fields + ("password1", "password2")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password1 = validated_data["password1"]
        password2 = validated_data["password2"]

        if password1 != password2:
            raise serializers.ValidationError({"password": "Password didn't match."})

        user = Recruiter(
            full_name=validated_data["full_name"],
            phone_number=validated_data["phone_number"],
            email=validated_data["email"],
            is_active=validated_data["is_active"],
            otp=get_random_string(6).upper(),
        )
        user.set_password(password1)
        user.save()
        return user
