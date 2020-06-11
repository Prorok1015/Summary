from __future__ import absolute_import, unicode_literals
import os
from celery import shared_task, Celery
from script.PageAlgoritm import Algoritm
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
app = Celery('my_app')
app.config_from_object('django.conf:settings')

do = Algoritm()

@app.task
def test():
    print("message")

@shared_task
def add_unical_pages_for_users():
    do.do()

