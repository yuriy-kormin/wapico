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