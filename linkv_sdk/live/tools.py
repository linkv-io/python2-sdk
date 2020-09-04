# -*- coding: UTF-8 -*-

import random
import time
import hashlib
from datetime import datetime


def genUniqueIDString(app_key):
    return '{}-{}'.format(
        app_key[2:],
        ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 9)),
    )


def genRandomString():
    return '{}{}{}'.format(
        ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 8)),
        str(int(time.mktime(datetime.now().timetuple()))),
        ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 8)))


def genSign(params, md5_secret):
    data = __encode(params) + "&key=" + md5_secret
    obj = hashlib.new('md5')
    obj.update(data.decode(encoding='utf8'))
    return obj.hexdigest().lower()


def __encode(params):
    keys = sorted(params.keys())
    container = ''
    for k in keys:
        if len(container) > 0:
            container += '&'
        container += '%s=%s' % (k, params[k])
    return container
