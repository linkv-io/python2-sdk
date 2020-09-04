# -*- coding: UTF-8 -*-

from .config import config
import time
import hmac
from datetime import datetime


class Rtc(object):
    def __init__(self):
        pass

    @staticmethod
    def genAuth():
        now = str(int(time.mktime(datetime.now().timetuple())))
        data = '{}{}'.format(config().app_id, now)
        auth_mac = hmac.new(config().app_key.encode('utf-8'), data.encode('utf-8'), digestmod='SHA1')
        return {
            'status': True,
            'app_id': config().app_id,
            'auth': auth_mac.hexdigest(),
            'expire_ts': now,
        }


class LvRTC(Rtc):
    def __init__(self):
        Rtc.__init__(self)

    def genAuth(self):
        return super(LvRTC, self).genAuth()
