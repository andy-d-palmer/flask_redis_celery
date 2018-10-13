from __future__ import absolute_import
from celery import Celery
app = Celery('celery_app',
             broker='amqp://admin:mypass@rabbit:5672',
             backend='redis://redis:6379/0',
             include=['tasks'])