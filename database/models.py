from datetime import datetime

from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

# todo: many-to-many relationship with Movies and Planets


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    opening_crawl = db.Column(db.Text)
    release_date = db.Column(db.DateTime)

    def __init__(self, title, opening_crawl, release_date):
        self.title = title
        self.opening_crawl = opening_crawl
        self.release_date = datetime(*map(int, release_date.split('-')))

    def __repr__(self):
        return '<Movie %r>' % self.title


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    diameter = db.Column(db.Integer)
    population = db.Column(db.Integer, default=None)

    def __init__(self, name, diameter, population):
        self.name = name
        self.diameter = int(diameter)
        if population.isdigit():
            self.population = int(population)

    def __repr__(self):
        return '<Planet %r>' % self.name
