from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initializes Flask app
app = Flask(__name__)
# Configures SQLAlchemy to use SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        # Represent Book object as a string
        return f"Book(id={self.id}, book_name='{self.book_name}', author='{self.author}', publisher='{self.publisher}')"

# Endpoint to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    new_book = Book(**data)
    db.session.add(new_book)
    db.session.commit()
    return jsonify({
        "id": new_book.id,
        "book_name": new_book.book_name,
        "author": new_book.author,
        "publisher": new_book.publisher
    }), 201

# Endpoint to get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{
        "id": book.id,
        "book_name": book.book_name,
        "author": book.author,
        "publisher": book.publisher
    } for book in books]), 200

# Endpoint to get a specific book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        "id": book.id,
        "book_name": book.book_name,
        "author": book.author,
        "publisher": book.publisher
    }), 200

# Endpoint to update a book by ID
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.json
    book.book_name = data.get('book_name', book.book_name)
    book.author = data.get('author', book.author)
    book.publisher = data.get('publisher', book.publisher)
    db.session.commit()
    return jsonify({
        "id": book.id,
        "book_name": book.book_name,
        "author": book.author,
        "publisher": book.publisher
    }), 200

# Endpoint to delete a book by ID
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)
