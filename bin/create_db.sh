if [ ! -d ./data ];
then
	mkdir ./data
	aws s3 cp s3://book-rec/books.csv ./data/books.csv
	aws s3 cp s3://book-rec/tfidf_sparse.npz ./data/tfidf_sparse.npz
	aws s3 cp s3://book-rec/vectorizer.pickle ./data/vectorizer.pickle
fi

sqlite3 app/app.db <<EOF
DROP TABLE IF EXISTS book;
CREATE TABLE book(
	id INTEGER PRIMARY KEY,
	title TEXT,
	author TEXT,
	n_pages TEXT,
	publisher TEXT,
	year INTEGER,
	rating NUMERIC,
	rating_count INTEGER,
	description TEXT,
	isbn_13 TEXT,
	isbn_10 TEXT,
	language TEXT,
	cover_img TEXT,
	genres TEXT,
	top_tfidf_words TEXT
);
.mode csv
.import data/books.csv book
EOF