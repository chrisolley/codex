./bin/create_db.sh

gunicorn --workers=4 --bind 0.0.0.0:${PORT:-8000} wsgi:app