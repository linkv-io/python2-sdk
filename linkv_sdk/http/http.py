# -*- coding: UTF-8 -*-

import urllib
import urllib2


class _HTTP:
    __slots__ = ['version']

    def __init__(self, version):
        self.version = version

    def get(self, uri='', params={}, headers={}):
        header = {
            'User-Agent': 'Python2 SDK v%s' % self.version,
        }
        header.update(headers)
        data = urllib.urlencode(params)
        request = urllib2.Request(uri + '?' + data, headers=header)
        return urllib2.urlopen(request)

    def post(self, uri='', params={}, headers={}):
        header = {
            'User-Agent': 'Python2 SDK v%s' % self.version,
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        header.update(headers)
        data = urllib.urlencode(params)
        request = urllib2.Request(uri, data=data, headers=headers)
        return urllib2.urlopen(request)


_http = None


def http(version=''):
    return _http if _http is not None else _HTTP(version)
