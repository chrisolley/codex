from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    n_pages = db.Column(db.Integer)
    publisher = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    rating_count = db.Column(db.Integer)
    description = db.Column(db.String)
    isbn_13 = db.Column(db.String)
    isbn_10 = db.Column(db.String)
    language = db.Column(db.String)
    cover_img = db.Column(db.String)
    genres = db.Column(db.String)
    top_tfidf_words = db.Column(db.String)

    def __repr__(self):
        return f'<Book: {self.title}>'
