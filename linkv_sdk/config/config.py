# -*- coding: UTF-8 -*-

from linkv_sdk.im.config import dict_config as dict_im_config
from linkv_sdk.rtc.config import dict_config as dict_rtc_config
from linkv_sdk.live.config import dict_config as dict_live_config
from linkv_sdk.http.http import http
from bindings.binding import download_library, binding
from json import loads


def init(app_id, app_secret, version):
    http(version)
    if not download_library():
        return False
    json_data = binding().decrypt(app_id, app_secret)
    d = loads(json_data)
    dict_im_config(d['im'] if 'im' in d.keys() else {})
    dict_rtc_config(d['rtc'] if 'rtc' in d.keys() else {})
    dict_live_config(d['sensor'] if 'sensor' in d.keys() else {})

    return True
