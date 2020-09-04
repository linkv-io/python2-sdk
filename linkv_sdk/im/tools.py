# -*- coding: UTF-8 -*-

import random
import string
import time


def genGUID():
    return '{}-{}-{}-{}'.format(
        ''.join(random.sample(string.ascii_letters + string.digits, 9)),
        ''.join(random.sample(string.ascii_letters + string.digits, 4)),
        ''.join(random.sample(string.ascii_letters + string.digits, 4)),
        ''.join(random.sample(string.ascii_letters + string.digits, 12)))


def getTimestampS():
    t = time.time()
    return str(int(t))


def getTimestampMS():
    t = time.time()
    return str(int(t * 1000))
