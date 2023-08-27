FROM python:3.11

# ENV DJANGO_SETTINGS_MODULE=moneybox.settings.production  TODO replace it as args
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY moneybox .
