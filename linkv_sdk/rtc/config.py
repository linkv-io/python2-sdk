# -*- coding: UTF-8 -*-

class _Config:
    __slots__ = ['app_id', 'app_key']

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key


_config = None


def config():
    return _config if _config is not None else None


def dict_config(d):
    app_id = d['app_id'] if 'app_id' in d.keys() else ''
    app_key = d['app_key'] if 'app_key' in d.keys() else ''
    global _config
    _config = _Config(app_id, app_key)
