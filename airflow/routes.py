from sanic import Blueprint

from api.v1 import search

api = Blueprint('api', url_prefix='/api/v1')

api.add_route(search.get_search, '/search/results/<search_id>/<currency>', methods=('GET',))
api.add_route(search.post_search, '/search', methods=('POST',))
