from database.models import Movie, Planet
from database import db


#--------------
# Movies
#--------------
def add_movie(data):
    title = data.get('title')
    opening_crawl = data.get('opening_crawl')
    release_date = data.get('release_date')

    movie = Movie(title, opening_crawl, release_date)

    db.session.add(movie)
    db.session.commit()


def update_movie(movie_id, data):
    movie = Movie.query.get(Movie.id == movie_id)
    movie.title = data.get('title')
    movie.opening_crawl = data.get('opening_crawl')
    movie.release_date = data.get('release_date')

    db.session.add(movie)
    db.session.commit()


def delete_movie(movie_id):
    movie = Movie.query.get(Movie.id == movie_id)

    db.session.delete(movie)
    db.session.commit()


#--------------
# Planets
#--------------
def add_planet(data):
    print(data)
    name = data.get('name')
    diameter = data.get('diameter')
    population = data.get('population')

    planet = Planet(name, diameter, population)

    db.session.add(planet)
    db.session.commit()


def update_planet(planet_id, data):
    planet = Planet.query.get(Planet.id == planet_id)
    planet.name = data.get('name')
    planet.diameter = data.get('diameter')
    planet.population = data.get('population')

    db.session.add(planet)
    db.session.commit()


def delete_planet(planet_id):
    planet = Planet.query.get(Planet.id == planet_id)

    db.session.delete(planet)
    db.session.commit()
