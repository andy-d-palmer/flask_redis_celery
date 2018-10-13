from __future__ import absolute_import
from celery import shared_task


@shared_task
def task1(s=""):
    return "task one did this. {}".format(s)


@shared_task
def task2():
    return "task two did this."


@shared_task
def task3():
    return task1("task three did this.")