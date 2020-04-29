from __future__ import absolute_import, unicode_literals

from celery import shared_task
from script.PageAlgoritm import Algoritm

do = Algoritm()

@shared_task
def test_task():
    do.do()

