from flask.ext.sqlalchemy import SQLAlchemy

from passlib.hash import bcrypt_sha256

import datetime
import hashlib

def sha512(string):
    return hashlib.sha512(string).hexdigest()

db = SQLAlchemy()

class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.String(80), unique=True)
    html = db.Column(db.Text)

    def __init__(self, route, html):
        self.route = route
        self.html = html

    def __repr__(self):
        return "<Tag {0} for challenge {1}>".format(self.tag, self.chal)

class Challenges(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.Text)
    value = db.Column(db.Integer) 
    category = db.Column(db.String(80))
    # add open category

    def __init__(self, name, description, value, category):
        self.name = name
        self.description = description
        self.value = value
        self.category = category

    def __repr__(self):
        return '<chal %r>' % self.name

class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.Text)
    value = db.Column(db.Text)

    def __init__(self, key, value):
        self.key = key
        self.value = value

