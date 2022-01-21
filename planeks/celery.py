# from __future__ import absolute_import, unicode_literals
#
# import os
#
# from celery import Celery
#
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planeks.settings')
# # BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
#
# app = Celery('planeks')
#
# app.conf.update(BROKER_URL='redis://:p71491f35d5901d262cac58655f3c6a859cb2addc23e69bc1c8732a873e46845c@ec2-3-248-5-190.eu-west-1.compute.amazonaws.com:9560',
#                 CELERY_RESULT_BACKEND='django-db')
#
#
# app.autodiscover_tasks()
