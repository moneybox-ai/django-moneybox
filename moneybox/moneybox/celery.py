import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moneybox.settings')

app = Celery('moneybox', broker='redis://127.0.0.1:6379')
app.config_from_object('django.conf:settings', namespace='CELERY')
#Celery.config_from_object(celeryconfig)
#app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')