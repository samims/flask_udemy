import sqlite3
from flask import Flask, render_template
from . import config

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)


@app.route('/')
def hello_world():
    db_connection = connect_db()
    cursor = db_connection.execute('SELECT id, name from author;')
    authors = [{'id': row[0], 'name': row[1]} for row in cursor.fetchall()]
    return render_template('database/authors.html', authors=authors)
