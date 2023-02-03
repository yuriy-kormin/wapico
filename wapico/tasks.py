# import json
from random import randint, sample
from celery import shared_task, group
from celery.result import AsyncResult

from wapico.whatsapp.models import Whatsapp
from wapico import celery_app as app
import requests
from time import sleep

# BASE_URL = 'https://ec170df6-51bf-477c-9423-660c26c877a0.mock.pstmn.io/send.php'
BASE_URL = 'http://127.0.0.1:8080/'


# @app.task(name ='simple')
@shared_task()
def add(x, y):
    return x + y


def make_request(whatsapp_id_from, whatsapp_id_to):
    instance_to = Whatsapp.objects.get(pk=whatsapp_id_to)
    instance_from = Whatsapp.objects.get(pk=whatsapp_id_from)
    # url = f'{BASE_URL}?number={instance_to.phone_number}' \
    #       f'&type=text&message={{здравствуйте}}&instance_id=' \
    #       f'{instance_from.instance}&access_token={instance_from.token}'
    url = f'{BASE_URL}?f={instance_from.id}&t={instance_to.id}'
    return requests.post(url=url).text


# @app.task(name='make dialog')
@app.task(name='group')
def process_group(id_from, ids, delay, time_delta):
    sleep(delay)
    responses = []
    for id in sample(ids, len(ids)):
        if id != id_from:
            responses.append(make_request(id_from, id))
            sleep(randint(*time_delta))
    return responses


@shared_task(name='task')
def process_task(*time_delta):
    ids = list(Whatsapp.objects.values_list('id', flat=True))

    if len(ids) < 2:
        return "error: we need at least 2 instances in whatsapp"

    result = group([
        process_group.s(
            v,
            ids,
            # randint(*time_delta)*i,
            5*i,
            time_delta
        ) for i, v in enumerate(ids)
    ])

    result.apply_async(add_to_parent=True)
    # result.apply_async(countdown=20)

    # while not result.ready():
    #     sleep(1)
    # result.
    return result

# AsyncResult('405fd771-a055-4cc5-a82f-d9ae917fee8c')
