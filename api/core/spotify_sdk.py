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

import requests
from base64 import b64encode

from const import Const


class SpotifySdk:
    @staticmethod
    def refresh_token():
        auth_str = f'{Const.SPOTIFY_CLIENT_ID}:{Const.SPOTIFY_SECRET_ID}'
        auth_ascii = b64encode(auth_str.encode()).decode('ascii')

        data = {
            'grant_type': 'refresh_token',
            'refresh_token': Const.SPOTIFY_REFRESH_TOKEN,
        }

        headers = {'Authorization': f'Basic {auth_ascii}'}
        response = requests.post(Const.REFRESH_TOKEN_URL, data=data, headers=headers)

        json_data = response.json()
        if 'access_token' in json_data:
            return json_data['access_token']
        else:
            raise KeyError('Access Token Not Found')

    @classmethod
    def recently_played(cls):
        """
        最近播放
        :return:
        """
        token = cls.refresh_token()
        url = f'{Const.SPOTIFY_DOMAIN}/v1/me/player/recently-played'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)

        if response.status_code == requests.status_codes.codes['no_content']:
            return dict()
        return response.json(), False

    @classmethod
    def now_playing(cls):
        """
        現在播放
        :return:
        """
        token = cls.refresh_token()
        url = f'{Const.SPOTIFY_DOMAIN}/v1/me/player/currently-playing'
        params = {
            'limit': 1
        }
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == requests.status_codes.codes['no_content']:
            return cls.recently_played()
        return response.json(), True
