# import json

import re
from random import randint, sample
from celery import shared_task, group
from celery.result import AsyncResult

from faker import Faker
from wapico.whatsapp.models import Whatsapp
from wapico.var.models import Var
from wapico import celery_app as app
import requests
from time import sleep

# BASE_URL = 'https://ec170df6-51bf-477c-9423-660c26c877a0.mock.pstmn.io/send.php'
BASE_URL = 'http://127.0.0.1:8080/'

faker = Faker('ru-Ru')


# @app.task(name ='simple')


def compile_url(url, phone_to):
    for var in Var.GENERATED_VARS:
        if var == 'message':
            message = faker.text(Var.FAKER_TEXT_LEN)
            url = re.sub('{{message}}', message, url)
        elif var == 'phone_number':
            url = re.sub('{{phone_number}}', phone_to, url)
        else:
            raise ValueError(f'parameter {var} did not set')
    return url


# @shared_task(name='request', bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_jitter=True,
#              retry_kwargs={'max_retries': 5})
def make_request(whatsapp_id_from, whatsapp_id_to): #, order_pos, time_delta):
    # sleep(order_pos * randint(*time_delta))
    instance_to = Whatsapp.objects.get(pk=whatsapp_id_to)
    instance_from = Whatsapp.objects.get(pk=whatsapp_id_from)
    url = compile_url(
        instance_from.get_url(),
        instance_to.phone_number
    )
    try:
        response = requests.post(url=url)
    except:
        raise Exception()
    if response.status_code != 200:
        raise Exception()
    return response.text


@app.task(name='group')
def process_group(id_from, ids, order_pos, time_delta):
    result = []
    sleep(order_pos * randint(*time_delta))
    for id_to in sample(ids, len(ids)):
        if id_to != id_from:
            result.append(
                make_request(id_from, id_to)
            )
            sleep(randint(*time_delta))
    return result
    # sleep(order_pos * randint(*time_delta))
    # result = group([
    #     make_request.s(
    #         whatsapp_id_from=id_from,
    #         whatsapp_id_to=v,
    #         order_pos=i+1,
    #         time_delta=time_delta,
    #     ) for i, v in enumerate(ids) if v != id_from
    # ])
    #
    # result.apply_async(add_to_parent=True)

    # return result


@shared_task(name='task')
def process_task(*time_delta):
    ids = list(Whatsapp.objects.values_list('id', flat=True))

    if len(ids) < 2:
        return "error: we need at least 2 instances in whatsapp"

    result = group([
        process_group.s(
            id_from=v,
            ids=ids,
            order_pos=i,
            time_delta=time_delta
        ) for i, v in enumerate(ids)
    ])

    result.apply_async(add_to_parent=True)
    return result

# AsyncResult('405fd771-a055-4cc5-a82f-d9ae917fee8c')
