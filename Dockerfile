FROM python:3.8

RUN mkdir /book-recommender-app
WORKDIR /book-recommender-app

COPY app ./app
COPY bin ./bin
COPY requirements.txt .
COPY wsgi.py .

RUN pip install -r requirements.txt

RUN apt-get clean && apt-get update
RUN apt-get install -y sqlite3 libsqlite3-dev

CMD ./bin/start.sh