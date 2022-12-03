from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from apps.users.choices import UserRoll
from apps.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    default_type = UserRoll.EMPLOYEE
    phone_regex = RegexValidator(
        regex=r"^(((?:\+88)?(?:\d{11}))|((?:01)?(?:\d{11})))$",
        message="Phone number must be entred in the format: +8801555555550, Up to 11 digits allowed.",
    )
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(
        validators=[phone_regex], max_length=14, unique=True
    )
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    roll = models.CharField(
        choices=UserRoll.choices, default=default_type, max_length=9
    )
    otp = models.CharField(max_length=6, blank=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    date_joined = models.DateTimeField(verbose_name="date join", auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"{self.phone_number}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.roll = self.default_type
        return super().save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True


class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(roll=UserRoll.EMPLOYEE)


class RecruiterManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(roll=UserRoll.RECRUITER)


class Employee(User):
    default_type = UserRoll.EMPLOYEE
    objects = EmployeeManager()

    class Meta:
        proxy = True


class Recruiter(User):
    default_type = UserRoll.RECRUITER
    objects = RecruiterManager()

    class Meta:
        proxy = True
