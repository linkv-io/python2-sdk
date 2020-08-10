# -*- coding: UTF-8 -*-

import config.config as config
from . import __version__
from im.im import LvIM
from rtc.rtc import LvRTC
from live.live import LvLIVE

OrderTypeAdd = 1
OrderTypeDel = 2

PlatformTypeH5 = 'h5'
PlatformTypeANDROID = 'android'
PlatformTypeIOS = 'ios'


def init(app_id, app_secret):
    return config.init(app_id, app_secret, __version__)
