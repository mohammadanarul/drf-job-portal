from rest_framework import serializers

from apps.job_portal.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            "user",
            "title",
            "vacancy",
            "skils",
            "address",
            "sellery",
            "country",
            "expiry_date",
            "description",
            "employees",
            "expiry",
        )