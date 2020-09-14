if [ ! -d ./data ];
then
	mkdir ./data
	aws s3 cp s3://book-rec/books.csv ./data/books.csv
	aws s3 cp s3://book-rec/tfidf_sparse.npz ./data/tfidf_sparse.npz
	aws s3 cp s3://book-rec/vectorizer.pickle ./data/vectorizer.pickle
fi

# docker build -t book-rec .
# docker run -d -p 5000:5000 book-rec
# sqlite3 app/app.db <<EOF
# .mode csv
# .import data/books.csv book
# EOF
./create_db.sh

gunicorn --workers=4 app:app