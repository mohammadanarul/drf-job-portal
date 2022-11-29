from django.db import models


class UserRoll(models.TextChoices):
    RECRUITER = "RECRUITER"
    EMPLOYEE = "EMPLOYEE"
