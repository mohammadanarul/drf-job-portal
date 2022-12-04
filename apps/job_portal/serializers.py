from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from apps.job_portal.models import Job


class JobSerializer(TaggitSerializer, serializers.ModelSerializer):
    country = CountryField()
    skils = TagListSerializerField()

    class Meta:
        model = Job
        fields = (
            "id",
            "user",
            "title",
            "vacancy",
            "skils",
            "address",
            "sellery",
            "country",
            "expiry_date",
            "description",
        )


class JobDetailSerializer(JobSerializer):
    class Meta(JobSerializer.Meta):
        fields = JobSerializer.Meta.fields + (
            "employees",
            "expiry",
        )
