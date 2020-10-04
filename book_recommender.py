from flask import current_app as app
from app import db
from app.models import Book


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Book': Book}
