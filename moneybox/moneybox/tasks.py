from celery import shared_task
from django_celery_beat.models import PeriodicTask


@shared_task(name="repeat_mess")
def repeat_mess():
    print('Test beats')
