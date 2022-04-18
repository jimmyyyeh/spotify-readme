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
from random import randint
from flask import render_template

from core.const import Const
from core.config import Config


class SvgHandler:

    @staticmethod
    def bar_generate(bar_count):
        """
        產生播放bar
        :param bar_count:
        :return:
        """
        bar_css = ""
        left = 1
        for i in range(1, bar_count + 1):
            anim = randint(1000, 1350)
            bar_css += (
                ".bar:nth-child({})  {{ left: {}px; animation-duration: {}ms; }}".format(
                    i, left, anim
                )
            )
            left += 4
        return bar_css

    @staticmethod
    def image_to_base64(url):
        """
        將圖檔轉成base64字串
        :param url:
        :return:
        """
        response = requests.get(url)
        return b64encode(response.content).decode('ascii')

    @classmethod
    def process_data(cls, data, is_current, data_dict, bar_count):
        """
        取得svg需要帶入的參數
        :param data:
        :param is_current:
        :param data_dict:
        :param bar_count:
        :return:
        """
        if is_current and data['item']:
            item = data['item']
        elif not is_current and Config.DISPLAY_RECENTLY:
            item = data['items'][0]['track']
        else:
            return
        artist_name = item['artists'][0]['name'].replace('&', '&amp;')
        song_name = item['name'].replace('&', '&amp;')
        image = cls.image_to_base64(item['album']['images'][1]['url'])
        bar_css = cls.bar_generate(bar_count=bar_count)
        data_dict.update({
            'image': image,
            'artist_name': artist_name,
            'song_name': song_name,
            'bar_css': bar_css
        })
        return data_dict

    @classmethod
    def make_svg(cls, data, is_current):
        """
        渲染svg
        :param data:
        :param is_current:
        :return:
        """
        bar_count = 84
        content_bar = ''.join(["<div class='bar'></div>" for _ in range(bar_count)])

        image = cls.image_to_base64(Const.LOADING_URL)
        bar_css = cls.bar_generate(bar_count=bar_count)
        data_dict = {
            'content_bar': content_bar,
            'image': image,
            'artist_name': 'Not Playing',
            'song_name': '',
            'bar_css': bar_css,
        }
        cls.process_data(data=data,
                         is_current=is_current,
                         data_dict=data_dict,
                         bar_count=bar_count)
        return render_template('spotify.html.j2', **data_dict)
