FROM python:3.9-alpine3.16


RUN apk add --no-cache postgresql-client build-base postgresql-dev

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password app-user
USER app-user

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
