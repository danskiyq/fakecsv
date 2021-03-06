from __future__ import absolute_import, unicode_literals

import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planeks.settings')
# BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('planeks')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()
