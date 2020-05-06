from sanic import Blueprint

from .search import search

api = Blueprint.group(search, url_prefix='/api')
