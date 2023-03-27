Django app to schedule communicate with wapico api

Project using redis as a broker and postgre as result

Tasks executed asynchronously with celery

To manipulate a schedule using django-celery-beat, which make possible to manipulate schedule as a django model instances

## RUN

need to run several process
- django  
  make start
- celery  
  make celery
- celery beat
  make scheduler
- flower ( option - running on port 81 - monitoring tool)  
  make flower

На данный момент получается что надо создать periodicTask к которому привязывается CronSchedule
Чтобы это сделать с помощью одной операции, нужно сделать форму, которая работает сразу с двумя моделями

есть варианты - добавить поля в форму( как сейчас сделано с minute_2)

есть аддон - https://django-betterforms.readthedocs.io/en/latest/
в нем есть возможность создать форму, которая будет работать сразу с несколькими моделями