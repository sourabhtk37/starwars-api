from flask_restplus import fields

from api.restplus import api

movie_fields = api.model('Movie list', {
    'title': fields.String,
    'opening_crawl': fields.String,
    'release_date': fields.String
})


planet_fields = api.model('Planet list', {
    'name': fields.String,
    'diameter': fields.String,
    'population': fields.String
})
