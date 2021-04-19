./bin/create_db.sh

gunicorn --workers=4 wsgi:app