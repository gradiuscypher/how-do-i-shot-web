#!/usr/bin/env python

from sanic import Sanic
from api import api

app = Sanic(__name__)

app.blueprint(api)
app.static('/static', './static')

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)
