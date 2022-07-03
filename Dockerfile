FROM python:3.9-slim-buster

RUN pip install pipenv

WORKDIR /app

COPY Pipfile /app
COPY Pipfile.lock /app
COPY *.py /app/
COPY templates /app/templates
COPY static /app/static
COPY forges /app/forges 


RUN pipenv install
RUN pipenv install gunicorn

ENTRYPOINT FLASK_APP=app FLASK_ENV=production pipenv run gunicorn -b 0.0.0.0:5000 app:app