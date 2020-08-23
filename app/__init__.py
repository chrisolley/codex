from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

import scipy.sparse
import pickle

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.tfidf = scipy.sparse.load_npz('./data/tfidf_sparse.npz')

with open('./data/vectorizer.pickle', 'rb') as f:
    app.vectorizer = pickle.load(f)
    app.vocab = app.vectorizer.get_feature_names()

from app import routes, models

