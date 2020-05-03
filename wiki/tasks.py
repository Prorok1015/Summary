from __future__ import absolute_import, unicode_literals

from celery import shared_task
from script.PageAlgoritm import Algoritm

do = Algoritm()

@shared_task
def add_unical_pages_for_users():
    do.do()

