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

import os


class Const:
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_SECRET_ID = os.getenv('SPOTIFY_SECRET_ID')
    SPOTIFY_REFRESH_TOKEN = os.getenv('SPOTIFY_REFRESH_TOKEN')
    DISPLAY_RECENTLY = os.getenv('DISPLAY_RECENTLY')
    DISPLAY_RECENTLY = bool(DISPLAY_RECENTLY) if DISPLAY_RECENTLY else None

    SPOTIFY_DOMAIN = 'https://api.spotify.com'
    SPOTIFY_LOGO = 'https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png'
    REFRESH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
    LOADING_URL = 'https://imgur.com/1jieQCA.png'
