FROM python:3.9.5-alpine3.13

ENV APP_HOME=/home/app

COPY ./apps/api $APP_HOME

RUN pip install --upgrade pip \
    && pip install -r $APP_HOME/requirements.txt \
    && pip install gunicorn==20.1.0

WORKDIR $APP_HOME

CMD gunicorn wsgi:app --bind 0.0.0.0:8000
