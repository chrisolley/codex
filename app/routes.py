from flask import current_app as app
from app.models import db, Book
from flask import render_template, jsonify, request
from sqlalchemy.sql.expression import func
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
import scipy
import pickle

app.tfidf = scipy.sparse.load_npz('./data/tfidf_sparse.npz')

with open('./data/vectorizer.pickle', 'rb') as f:
    app.vectorizer = pickle.load(f)

app.vocab = app.vectorizer.get_feature_names()


@app.route('/')
def index():
    random_books = Book.query.order_by(func.random()).limit(12)
    return render_template('index.html', random_books=random_books)


@app.route('/book/<int:book_id>')
def book(book_id):
    book = Book.query.filter_by(id=book_id).one()
    k_nearest_books = get_k_nearest_books(book_id)
    return render_template('book.html', book=book, nearest_books=k_nearest_books)


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    query = db.session.query(Book.id, Book.title).filter(Book.title.like('%' + str(search) + '%'))
    results = [{'label': b[1], 'value': b[0]} for b in query.all()]
    return jsonify(matching_results=results)


@app.route('/load_more_books', methods=['GET'])
def load_more_books():
    random_books = Book.query.order_by(func.random()).limit(12)
    html = ""
    for i in range(3):
        html += """<div class="row">"""
        for book in random_books[i:i+3]:
            html += f"""
                <div class="col-sm-4 mb-5">
                    <div class="card">
                        <a href="book/{book.id}"><img src="{book.cover_img}" class="card-img-top" alt="book_cover"></a>
                        <div class="card-body">
                            <h5 class="card-title text-center"><a href="book/{book.id}">{book.title}</a></h5>
                        </div>
                    </div>
                </div>
            """
        html += """</div>"""
    return html


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('images/book.png')


def get_k_nearest_books(book_id, k=5):
    similarity = linear_kernel(app.tfidf[book_id], app.tfidf).flatten()
    indices = np.argsort(similarity)[-k-1:-1][::-1].tolist()
    scores = similarity[indices]
    books = Book.query.filter(Book.id.in_(indices)).all()
    return [
        {
            'id': book.id,
            'title': book.title,
            'score': score,
            'similar_words': ', '.join(get_k_similar_words(book.id, book_id))
        } for book, score in zip(books, scores)
    ]


def get_k_similar_words(book_id_1, book_id_2, k=5):
    element_indices = list(np.argsort(np.multiply(app.tfidf[book_id_1].toarray().flatten(),
                                                  app.tfidf[book_id_2].toarray().flatten()))[-k:][::-1])
    return [app.vocab[i] for i in element_indices]
