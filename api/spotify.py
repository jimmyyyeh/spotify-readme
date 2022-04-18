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

from flask import Flask, Response
from core.spotify_sdk import SpotifySdk
from core.svg_handler import SvgHandler

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_spotify_status(path):
    data, is_current = SpotifySdk.now_playing()
    svg = SvgHandler.make_svg(data, is_current)

    response = Response(svg, mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 's-maxage=1'

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False)
