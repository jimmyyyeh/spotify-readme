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


class Config:
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_SECRET_ID = os.getenv('SPOTIFY_SECRET_ID')
    SPOTIFY_REFRESH_TOKEN = os.getenv('SPOTIFY_REFRESH_TOKEN')
    DISPLAY_RECENTLY = os.getenv('DISPLAY_RECENTLY')
    DISPLAY_RECENTLY = bool(DISPLAY_RECENTLY) if DISPLAY_RECENTLY else None
    ENVIRONMENT = os.getenv('ENV', 'develop')
