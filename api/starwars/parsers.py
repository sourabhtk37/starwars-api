from flask_restplus import reqparse

search_query = reqparse.RequestParser()
search_query.add_argument(
    'search', required=False, default='', help='Search string')
