from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.job_portal.models import Job
from apps.job_portal.serializers import JobSerializer


class JobPortalListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
