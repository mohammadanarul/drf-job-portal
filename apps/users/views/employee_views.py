from django.utils.crypto import get_random_string
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.users.models import Employee
from apps.users.serializers.employee_serializers import (
    EmployeeRegisterSerializer,
    EmployeeSerializer,
)
from apps.users.tasks import create_profile_and_send_otp_mail


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return EmployeeSerializer
        if self.request.method == "PUT":
            return EmployeeSerializer
        else:
            return EmployeeRegisterSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        create_profile_and_send_otp_mail.delay(obj.pk)


class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "pk"
