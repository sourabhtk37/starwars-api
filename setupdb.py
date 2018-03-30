# WIP: figuring out ways to populate DB.
import requests
from flask_restplus import fields
import sqlalchemy

from api.restplus import api
from database.models import Movie, Planet
from database import db

movie_fields = api.model('Movie list', {
    'title': fields.String,
    'opening_crawl': fields.String,
    'release_date': fields.String
})


@api.marshal_with(movie_fields)
def get_movies():
    """
    Returns a blog post.
    """
    response_movies = requests.get('https://swapi.co/api/films')

    return response_movies.json()['results']


def add_mv_db(movies):
    for movie in movies:
        post = Movie(movie['title'],
                     movie['opening_crawl'],
                     movie['release_date'])
        db.session.add(post)
        db.session.commit()
        return post


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    movies = get_movies()
    add_mv_db(movies)
    print(Movie.query.all())
