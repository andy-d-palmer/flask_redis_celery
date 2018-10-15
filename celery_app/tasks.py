from __future__ import absolute_import
from celery import shared_task
from celery_app import app


@app.task(name='q2:task1')
def task1(s=""):
    return "task one did this in queue2. {}".format(s)


@app.task(name='q2:task2')
def task2():
    return "task two did this in queue2."


@app.task(name='q1:task3')
def task3():
    return task1("task three did this in queue1.")