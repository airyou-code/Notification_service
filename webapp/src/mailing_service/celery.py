import os

from celery import Celery
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailing_service.settings')

app = Celery('mailing_service')

app.config_from_object('django.conf:settings', namespace='CELERY')
# celery -A mailing_service beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
# celery -A mailing_service worker -l INFO
# docker run -d -p 5672:5672 rabbitmq
# Load task modules from all registered Django apps.
app.conf.timezone = 'UTC'
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')