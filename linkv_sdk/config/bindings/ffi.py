# -*- coding: UTF-8 -*-

import platform
import os
from requests import get
from tempfile import gettempdir
from ctypes import CDLL


def _platform_file(name):
    ext = ''

    if platform.uname()[0] == "Linux":
        ext = 'so'
    elif platform.uname()[0] == "Darwin":
        ext = 'dylib'
    elif platform.uname()[0] == "Windows":
        ext = 'dll'

    return "lib{}.{}".format(name, ext)


def dlopen_platform_specific(name, path):
    return CDLL('{}/{}'.format(gettempdir() if path == "" else path, _platform_file(name)))


DownloadURL = 'http://dl.linkv.fun/static/server'


def download(name, path, version):
    filepath = '{}/{}'.format(gettempdir() if path == "" else path, _platform_file(name))
    if os.path.exists(filepath):
        return True

    r = get('{}/{}/{}'.format(DownloadURL, version, _platform_file(name)))

    if r.status_code != 200:
        return False

    with open(filepath, 'wb') as f:
        f.write(r.content)

    r.close()
    return True
