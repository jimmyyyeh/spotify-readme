# -*- coding: utf-8 -*
"""
      ┏┓       ┏┓
    ┏━┛┻━━━━━━━┛┻━┓
    ┃      ☃      ┃
    ┃  ┳┛     ┗┳  ┃
    ┃      ┻      ┃
    ┗━┓         ┏━┛
      ┗┳        ┗━┓
       ┃          ┣┓
       ┃          ┏┛
       ┗┓┓┏━━━━┳┓┏┛
        ┃┫┫    ┃┫┫
        ┗┻┛    ┗┻┛
    God Bless,Never Bug
"""
from spotify import app
from core.svg_handler import SvgHandler
from core.spotify_sdk import SpotifySdk
from flask import Response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_spotify_status(path):
    data, is_current = SpotifySdk.now_playing()
    svg = SvgHandler.make_svg(data, is_current)

    response = Response(svg, mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 's-maxage=1'

    return response
