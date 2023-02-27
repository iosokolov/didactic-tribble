from sanic import Blueprint

from api.v1 import search
from srv.v1 import health_check

# api = Blueprint('api', url_prefix='/api/v1')
# api.add_route(search.get_search, '/search/results/<search_id>/<currency>', methods=('GET',))
# api.add_route(search.post_search, '/search', methods=('POST',))

api = Blueprint('api', url_prefix='/')
api.add_route(search.get_search, '/results/<search_id>/<currency>', methods=('GET',))
api.add_route(search.post_search, '/search', methods=('POST',))

srv = Blueprint('srv', url_prefix='/srv/v1')
srv.add_route(health_check.ping, '/ping', methods=('GET',))
