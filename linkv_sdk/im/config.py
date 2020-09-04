# -*- coding: UTF-8 -*-

class _Config:
    __slots__ = ['app_id', 'app_key', 'app_secret', 'url']

    def __init__(self, app_id, app_key, app_secret, url):
        self.app_id = app_id
        self.app_key = app_key
        self.app_secret = app_secret
        self.url = url


_config = None


def config():
    return _config if _config is not None else None


def dict_config(d):
    app_id = d['app_id'] if 'app_id' in d.keys() else ''

    app_key = d['app_key'] if 'app_key' in d.keys() else ''
    app_secret = d['app_secret'] if 'app_secret' in d.keys() else ''
    url = d['url'] if 'url' in d.keys() else ''

    app_id = 'linkvim'
    app_key = '41160b64'
    app_secret = 'a9867322c6567852fec8309fa183c883'
    url = 'http://catchu-im-api.fusionv.com'
    global _config
    _config = _Config(app_id, app_key, app_secret, url)
