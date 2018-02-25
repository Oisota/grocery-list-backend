import sqlite3 as sql
from contextlib import contextmanager

from flask import g

from . import app

def dict_factory(cursor, row):
    """Convert db row into dict"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def init_db():
    """Create empty database tables"""
    with app.app_context():
        db = get_db()
        with app.open_resource(app.config['SCHEMA'], mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    """Set the _db attribute on the flask global object"""
    db = getattr(g, '_db', None)
    if db is None:
        db = g._db = sql.connect(app.config['DB'])
        db.row_factory = dict_factory
    return db

@app.teardown_appcontext
def close_db(exception):
    """Close the db connection when the request is done"""
    db = getattr(g, '_db', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    """Execute db queries"""
    cur = get_db().cursor()
    cur.execute(query, args)
    if one:
        res = cur.fetchone()
    else:
        res = cur.fetchall()
    cur.close()
    return res if res else None

@contextmanager
def db_commit():
    """get a db cursor that is auto committed"""
    con = get_db()
    yield con.cursor()
    con.commit()
