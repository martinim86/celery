"""
Celery config file

https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html

"""
from django.conf import settings
from datetime import timedelta
import os
from celery import Celery
from celery.schedules import crontab

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_example.settings')

# you change change the name here
app = Celery("django_celery_example")

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# load tasks.py in django apps
app.autodiscover_tasks()

from django.core.mail import send_mail, EmailMultiAlternatives

RECIPIENTS_EMAIL = ['manager@mysite.com']


@app.task
def send_email(x, y):
    with open('readmewerfsdfs.txt', 'w') as f:
        f.write('Create a new text file!')

    return x / y


task = send_email.delay(10, 2)
app.conf.beat_shedule = {
    'send_spam':{
        'task' : 'send_email',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    }
}

# @app.task
# def add():
#     with open('readmewerfsdfs.txt', 'w') as f:
#         f.write('Create a new text file!')
# Create your views here.


# from django.core.mail import send_mail, EmailMultiAlternatives
# RECIPIENTS_EMAIL = ['manager@mysite.com']
# @app.task
# def send():
#     # msg = EmailMultiAlternatives('its send function' '123', '123@gmail.com', RECIPIENTS_EMAIL)
#     # msg.send()
#     print('its sand f')
