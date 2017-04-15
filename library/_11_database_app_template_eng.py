import sqlite3
from flask import Flask, g, render_template
from . import config

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)


@app.before_request
def before_request():
    g.db = connect_db()


@app.route('/')
def hello_world():
    cursor = g.db.execute('select id, name from author;')
    authors = [dict(id=row[0], name = row[1]) for row in cursor.fetchall()]
    return render_template('database/authors_with_conditional.html',authors=authors)


@app.route('/extra')
def extra():
    return "Other view"