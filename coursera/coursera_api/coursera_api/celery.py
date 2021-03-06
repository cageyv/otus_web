import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursera_api.settings')

os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

import configurations
configurations.setup()

app = Celery('coursera_api')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()
