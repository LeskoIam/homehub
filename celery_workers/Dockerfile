FROM python:3.9-alpine

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

COPY . /celery-workers
WORKDIR /celery-workers

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
