import string

from celery import shared_task
from django.utils.crypto import get_random_string


@shared_task
def create_random_number(total):
    num = get_random_string(12)
    print("i am working celery.....", num.upper())
