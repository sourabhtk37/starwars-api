import logging

import requests
from flask import request
from flask_restplus import Resource, fields

from api.restplus import api
from api.starwars.parsers import search_query
from api.starwars.serialisers import movie_fields
from api.starwars.business import add_movie, update_movie, delete_movie
from database import db
from database.models import Movie

log = logging.getLogger(__name__)

ns = api.namespace('starwars/movies', description='Star wars Movies')


@ns.route('/')
class MovieCollection(Resource):

    @api.expect(search_query)
    @api.marshal_with(movie_fields)
    def get(self):
        """Returns list of movies"""
        args = search_query.parse_args(request)
        search_args = args.get('search', '')
        response_movies = requests.get(
            'https://swapi.co/api/films?search=%s' % search_args)

        return response_movies.json()['results']

    @api.expect(movie_fields)
    @api.response(201, "Movie added successfully")
    def post(self):
        """Adds movie to the favourite list"""
        add_movie(request.json)

        return None, 201


@ns.route('/<int:id>')
class MovieItem(Resource):

    @api.marshal_with(movie_fields)
    def get(self, id):
        """Returns movie"""
        response_movies = requests.get('https://swapi.co/api/films/%s' % id)

        return response_movies.json()

    @api.response(201, "Movie added successfully")
    def post(self, id):
        """Adds movie to the favourite list"""
        response_movie = requests.get('https://swapi.co/api/films/%s' % id)
        add_movie(response_movie.json())

        return None, 201


@ns.route('/favourite/<int:id>')
class MovieFav(Resource):

    @api.marshal_with(movie_fields)
    def get(self, id=None):
        """Returns favourite movies"""
        if id:
            return Movie.query.filter(Movie.id == id).one()
        return Movie.query.all()

    @api.expect(movie_fields)
    @api.response(204, 'Movie successfully updated')
    def put(self, id):
        """Updates favourite movie details"""
        update_movie(id, request.json)

        return None, 204

    @api.response(204, 'Movie successfully deleted.')
    def delete(self, id):
        """Delete movie from favourite movies"""
        delete_movie(id)
        
        return None, 204
