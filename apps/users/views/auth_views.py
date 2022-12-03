from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.serializers.auth_serializers import OTPSerializer
from apps.users.serializers.employee_serializers import EmployeeSerializer


class OTPVerify(APIView):
    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(otp=serializer.data["otp"])
                if user.is_active:
                    return Response(
                        {
                            "message": "Alredy Your Account Activated...",
                            "status": status.HTTP_200_OK,
                        }
                    )
                user.is_active = True
                user.otp = ""
                user.save()
            except User.DoesNotExist:
                return Response(
                    {
                        "message": "Your OTP Not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    }
                )
            return Response(
                {
                    "message": "successfully activated your account.",
                    "status": status.HTTP_200_OK,
                }
            )
