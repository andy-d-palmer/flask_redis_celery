from __future__ import absolute_import
from celery import Celery
from kombu import Queue

app = Celery('celery_app',
             broker='amqp://admin:mypass@rabbit:5672',
             backend='redis://redis:6379/0',
             include=['tasks'])

app.conf.update({
    'task_routes': ('task_router.TaskRouter',),
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['json']})