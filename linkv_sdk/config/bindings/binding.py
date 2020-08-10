# -*- coding: UTF-8 -*-

from ffi import dlopen_platform_specific, download
from ctypes import c_char_p, c_void_p, cast

VERSION = '0.0.4'
FILE = 'decrypt'


class _Binding:
    core = None

    def __init__(self):
        self.core = dlopen_platform_specific(FILE, '')

    def decrypt(self, app_id, app_secret):
        self.core.decrypt.argtypes = [c_char_p, c_char_p]
        self.core.decrypt.restype = c_void_p
        ptr = self.core.decrypt(app_id.encode('utf-8'), app_secret.encode('utf-8'))
        app_config = cast(ptr, c_char_p).value
        self.core.release.argtypes = c_void_p,
        self.core.release.restype = None
        self.core.release(ptr)
        return app_config


def download_library():
    return download(FILE, "", VERSION)


_binding = None


def binding():
    global _binding
    if _binding:
        return _binding
    _binding = _Binding()
    return _binding
