from celery_app import app
from tasks import task1, task2, task3
print('running tasks')

print(task1.delay().get())
print(task2.delay().get())
print(task3.delay().get())

print('tasks ran')
