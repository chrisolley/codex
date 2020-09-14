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