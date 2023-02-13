# Wayne Bell 02-13-2023
# This program uses a crud api to create, read, update, and delete data from a database
# The database uses a model for a book with the following parameters: id, book_name, author, publishor and year published

# Import the necessary modules from flask
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Create an empty list of books
books = []

# Create a class for the book model
class Book(Resource):
    def get(self, id):
        for book in books:
            if book['id'] == id:
                return book, 200
        return 'Book not found', 404

    # Create a post method to add a book to the database
    def post(self, id):
        book = {'id': id,
                'book_name': request.form['book_name'],
                'author': request.form['author'],
                'publisher': request.form['publisher'],
                'year_published': request.form['year_published']}
        books.append(book)
        return book, 201

    # Create a put method to update a book in the database
    def put(self, id):
        for book in books:
            if book['id'] == id:
                book['book_name'] = request.form['book_name']
                book['author'] = request.form['author']
                book['publisher'] = request.form['publisher']
                book['year_published'] = request.form['year_published']
                return book, 200
        return 'Book not found', 404

    # Create a delete method to delete a book from the database
    def delete(self, id):
        global books
        books = [book for book in books if book['id'] != id]
        return '', 204

# Create a route for the book class
api.add_resource(Book, '/book/<int:id>')

# Create a route for the home page
if __name__ == '__main__':
    app.run(debug=True)
