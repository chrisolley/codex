FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

RUN apt-get clean && apt-get update
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN create_db.sh

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app"]