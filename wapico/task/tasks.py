import json
from random import randint
from celery import shared_task
from wapico.whatsapp.models import Whatsapp
import requests
from time import sleep


@shared_task()
def make_result(time_1=60, time_2=70):
    result = []
    objects = list(Whatsapp.objects.all())
    for obj in objects:
        for obj_send in objects:
            if obj_send is obj:
                continue
            url = 'https://ec170df6-51bf-477c-9423-660c26c877a0.mock.pstmn.io/send.php'
            url += f'?number={obj_send.phone_number}'
            url += '&type=text&message={здравствуйте}'
            url += f'&instance_id={obj.instance}&access_token={obj.token}'

            resp = requests.post(url=url)
            delay = randint(time_1, time_2)
            # result.append({
            #     'operation': f'{obj.phone_number} -> {obj_send.phone_number} with delay {delay}',
            #     'res': json.loads(resp.content)
            # })
            result.append(resp.json())
            # sleep(delay)
    return result
