AWS_ACCESS_KEY_ID=$(aws --profile default configure get aws_access_key_id)
AWS_SECRET_ACCESS_KEY=$(aws --profile default configure get aws_secret_access_key)

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

gunicorn --workers=4 --bind=0.0.0.0:5000 app:app