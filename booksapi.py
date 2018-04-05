import os
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps

e = create_engine('sqlite:///' + os.getcwd() + '/books.db')

app = Flask(__name__)
api = Api(app)

class BooksIndex(Resource):
    """
    Shows every book on the list.
    ISBN, Title, Author
    """
    def get(self):
        conn = e.connect()
        query = conn.execute("SELECT title, author, isbn FROM books")
        return {
        	'book-list': [dict(zip(tuple(query.keys()), i)) for i in query.cursor.fetchall()]
        }


class BooksGet(Resource):

    def get(self, isbn):
        conn = e.connect()
        query = conn.execute("SELECT * FROM books WHERE isbn LIKE '{}%'".format(isbn))
        return {
        	'book': [dict(zip(tuple(query.keys()), i)) for i in query.cursor.fetchall()]
        }

class BooksAdd(Resource):
    """
    Add another book on the list.
    """
    def post(self):
        #On terminal
        #curl http://127.0.0.1:5000/add -d "isbn=9788498721805&title=El psicoanalista&author=John Katzenbach&editorial=Zeta&date_edition=07-2017&lenguage=español" -X POST -v
        #or
        #curl -d '{"isbn":"9786078126842", "title":"Lolita", "author":"Vladimir Nabokov", "editorial": "Anagrama", "date_edition":"03-2017", "lenguage":"español" }' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/add

        parser = reqparse.RequestParser()
        parser.add_argument('isbn')
        parser.add_argument('title')
        parser.add_argument('author')
        parser.add_argument('editorial')
        parser.add_argument('date_edition')
        parser.add_argument('lenguage')
        args = parser.parse_args()

        conn = e.connect()

        conn.execute("INSERT INTO books(isbn, title, author, editorial, date_edition, lenguage) VALUES("
            + "'" + args['isbn'] + "',"
            + "'" + args['title'] + "',"
            + "'" + args['author'] + "',"
            + "'" + args['editorial'] + "',"
            + "'" + args['date_edition'] + "',"
            + "'" + args['lenguage'] + "')")
        
        return "New book! {} of {}.".format(args['title'], args['author'])


class BooksReadOne(Resource):

    #curl http://127.0.0.1:5000/9786078126842/read -X PUT
    def put(self, isbn):
        """parser = reqparse.RequestParser()
        parser.add_argument('read')
        args = parser.parse_args()"""
        conn = e.connect()
        conn.execute("UPDATE books SET read=1 WHERE isbn='{}'".format(isbn))
        return "Book {} changed 'unread' to 'read'.".format(isbn)

class BooksUpdate(Resource):

    #curl http://127.0.0.1:5000/update/9786078126842 -d "author=10000" -X PUT

    def put(self, isbn):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        parser.add_argument('author')
        parser.add_argument('editorial')
        parser.add_argument('date_edition')
        parser.add_argument('lenguage')
        parser.add_argument('read')
        parser.add_argument('info')
        args = parser.parse_args()

        conn = e.connect()
        conn.execute("UPDATE books SET"
            + ((" title='"+ args['title'] +"'") if args['title'] else '')  
            + ((" author='"+ args['author'] +"'") if args['author'] else '')
            + ((" editorial='"+ args['editorial'] +"'") if args['editorial'] else '')
            + ((" date_edition='"+ args['date_edition'] +"',") if args['date_edition'] else '')
            + ((" lenguage='"+ args['lenguage'] +"'") if args['lenguage'] else '')
            + ((" read='"+ int(args['read']) +"'") if args['read'] else '')
            + ((" info='"+ args['info'] +"'") if args['info'] else '')
            + " WHERE isbn='{}'".format(isbn))

        return "Book {} updated!".format(isbn)

class BooksDelete(Resource):

    #curl http://127.0.0.1:5000/9788408045076/delete -X DELETE -v
    def delete(self, isbn):
        conn = e.connect()
        conn.execute("DELETE FROM books WHERE isbn='{}'".format(isbn))
        return 'Book {} deleted!'.format(isbn)

api.add_resource(BooksIndex, '/')
api.add_resource(BooksGet, '/<string:isbn>')
api.add_resource(BooksReadOne, '/<string:isbn>/read')
api.add_resource(BooksUpdate, '/update/<string:isbn>')
api.add_resource(BooksAdd, '/add')
api.add_resource(BooksDelete, '/<string:isbn>/delete')

if __name__ == '__main__':
    app.run(debug=True)