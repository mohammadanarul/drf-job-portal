from django.db import models
from django_countries.fields import CountryField
from taggit.managers import TaggableManager

from apps.common.models import BaseModel
from apps.users.models import Employee, Recruiter


class Job(BaseModel):
    user = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    vacancy = models.IntegerField()
    skils = TaggableManager()
    address = models.CharField(max_length=150)
    sellery = models.CharField(max_length=30)
    country = CountryField(blank_label="(select country)")
    expiry_date = models.DateField()
    description = models.TextField()
    employees = models.ManyToManyField(Employee, related_name="job_applies")
    expiry = models.BooleanField(default=False)

    def __str__(self):
        return self.title
