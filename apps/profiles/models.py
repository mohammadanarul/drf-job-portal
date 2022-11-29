from django.db import models
from django_countries.fields import CountryField

from apps.common.models import BaseModel
from apps.users.models import Employee, Recruiter


class RecruiterProfile(BaseModel):
    user = models.OneToOneField(Recruiter, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250)
    website_url = models.URLField(max_length=255)
    country = CountryField(blank_label="(select country)")


class EmployeeProfile(BaseModel):
    user = models.OneToOneField(Employee, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    cv_pdf = models.FileField(upload_to="cv-pdf/")
    skils = TaggableManager()
    bio = models.TextField()
    country = CountryField(blank_label="(select country)")
