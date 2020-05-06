from sanic import Blueprint
from sanic.response import json

search = Blueprint('search', url_prefix='/search')


@search.route('/', methods=['GET'])
async def index(request):
    return json({'search': 'index'})
