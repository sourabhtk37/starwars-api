import logging
import requests

from flask import request
from flask_restplus import Resource

from api.restplus import api
from api.starwars.business import add_planet, delete_planet, update_planet
from api.starwars.parsers import search_query
from api.starwars.serialisers import planet_fields
from database import db
from database.models import Planet

log = logging.getLogger(__name__)

ns = api.namespace('starwars/planets', description='Star Wars Planets')


@ns.route('/')
class PlanetCollection(Resource):

    @api.expect(search_query)
    @api.marshal_with(planet_fields)
    def get(self):
        """Returns list of planets"""
        args = search_query.parse_args(request)
        search_args = args.get('search', '')
        response_planets = requests.get(
            'https://swapi.co/api/planets?search=%s' % search_args)

        return response_planets.json()['results']

    @api.expect(planet_fields)
    @api.response(201, "planet added successfully")
    def post(self):
        """Adds planet to the favourite list"""
        add_planet(request.json)

        return None, 201


@ns.route('/<int:id>')
class PlanetItem(Resource):

    @api.marshal_with(planet_fields)
    def get(self, id):
        """Returns planet"""
        response_planets = requests.get('https://swapi.co/api/planets/%s' % id)

        return response_planets.json()

    @api.response(201, "planet added successfully")
    def post(self, id):
        """Adds planet to the favourite list"""
        response_planet = requests.get('https://swapi.co/api/planets/%s' % id)
        add_planet(response_planet.json())

        return None, 201


@ns.route('/favourite/<int:id>')
class PlanetFav(Resource):

    @api.marshal_with(planet_fields)
    def get(self, id=None):
        """Returns favourite planets"""
        if id:
            return Planet.query.filter(Planet.id == id).one()
        return Planet.query.all()

    @api.expect(planet_fields)
    @api.response(204, 'planet successfully updated')
    def put(self, id):
        """Updates favourite planet details"""
        update_planet(id, request.json)

        return None, 204

    @api.response(204, 'planet successfully deleted.')
    def delete(self, id):
        """Delete planet from favourite planets"""
        delete_planet(id)

        return None, 204
