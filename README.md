# Codex

### https://codex-book-app.herokuapp.com/

Codex is a simple book recommender app created to test some NLP techniques on scraped book data, as well as deployment strategies for Flask apps.

## Installation

To run Codex yourself, install the requirements using `pip`:

```
pip install -r requirements.txt
```

Then, run the start up script to download data files from S3, create a SQLite database and start the Flask app using a [Gunicorn](https://gunicorn.org/) WSGI server.

```
./bin/start.sh
```

You can also run the application using [Docker](https://docs.docker.com/get-docker/), using something like:

```
docker build -t cortex
docker run -p 8000:8000 -v ~/.aws:/root/.aws:ro cortex
```

where the second command assumes you have AWS credentials at the appropriate location, for downloading data from S3.

