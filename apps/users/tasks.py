from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from apps.profiles.models import EmployeeProfile, RecruiterProfile
from apps.users.choices import UserRoll
from apps.users.models import User


@shared_task
def create_profile_and_send_otp_mail(user_id):
    """profile create and send activation otp mail..."""
    user = User.objects.get(pk=user_id)

    if user.roll == UserRoll.EMPLOYEE:
        EmployeeProfile.objects.create(user=user)
    else:
        RecruiterProfile.objects.create(user=user)

    subject = "Congratulations Email activation Code."
    message = f"Hi {user.full_name}, click on the link to activate OTP: {user.otp}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)
