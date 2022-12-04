from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.job_portal.models import Job
from apps.job_portal.serializers import JobDetailSerializer, JobSerializer
from apps.job_portal.tasks import job_notification_to_employee


class JobPortalListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return JobDetailSerializer
        else:
            return JobSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        job_notification_to_employee.delay(obj.id)


class JobPortalRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return JobSerializer
        else:
            return JobDetailSerializer
