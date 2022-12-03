from django.utils.crypto import get_random_string
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.users.models import Recruiter
from apps.users.serializers.recruiter_serializers import (
    RecruiterRegisterSerializer,
    RecruiterSerializer,
)
from apps.users.tasks import create_profile_and_send_otp_mail


class RecruiterListView(generics.ListCreateAPIView):
    queryset = Recruiter.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RecruiterSerializer
        else:
            return RecruiterRegisterSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        create_profile_and_send_otp_mail.delay(obj.pk)


class RecruiterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"
