import string

from celery import shared_task
from django.utils.crypto import get_random_string


@shared_task
def create_random_number(nums):
    return f"i am working celery.....num:{get_random_string(nums).upper()}"
