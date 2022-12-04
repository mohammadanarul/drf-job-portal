import json

from celery import shared_task
from django.conf import settings
from django.core import serializers
from django.core.mail import send_mail

from apps.job_portal.models import Job
from apps.job_portal.utils import unique_items
from apps.profiles.models import EmployeeProfile


@shared_task
def job_notification_to_employee(job_id):
    job = Job.objects.get(id=job_id)
    employees = EmployeeProfile.objects.filter(skils__in=job.skils.all())
    email_list = []
    for employee in employees:
        email_list.append(employee.user.email)
    # mail send to employees
    subject = "Your job alert, Match your preferences."
    message = f"""
    url: http://127.0.0.1:8000/jobs/{job.id}/
    """
    email_from = settings.EMAIL_HOST_USER
    recipient_list = unique_items(email_list)
    send_mail(subject, message, email_from, recipient_list)
