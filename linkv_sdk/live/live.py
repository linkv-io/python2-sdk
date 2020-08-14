# -*- coding: UTF-8 -*-

import random
import json
import time
import hashlib
from datetime import datetime

from .config import config
from linkv_sdk.http.http import http

SexTypeUnknown = int(-1)
SexTypeFemale = int(0)
SexTypeMale = int(1)

OrderTypeAdd = int(1)
OrderTypeDel = int(2)

PlatformTypeH5 = str('h5')
PlatformTypeANDROID = str('android')
PlatformTypeIOS = str('ios')

waitTime = 0.3


class Live(object):
    def __init__(self):
        pass

    @staticmethod
    def GetTokenByThirdUID(third_uid, a_id, user_name='', sex=SexTypeUnknown, portrait_uri='', user_email='',
                           country_code='', birthday=''):
        nonce = genRandomString()
        params = {
            'nonce_str': nonce,
            'app_id': config().app_key,
            'userId': third_uid,
            'aid': a_id,
        }
        if len(user_name) > 0:
            params['name'] = user_name

        if len(portrait_uri) > 0:
            params['portraitUri'] = portrait_uri

        if len(user_email) > 0:
            params['email'] = user_email

        if len(country_code) > 0:
            params['countryCode'] = country_code

        if len(birthday) > 0:
            params['birthday'] = birthday

        if sex != SexTypeUnknown:
            params['sex'] = str(sex)

        params['sign'] = genSign(params, config().app_secret)

        uri = config().url + '/open/v0/thGetToken'

        err_result = ''
        i = 0
        while i < 3:
            response = http().post(uri=uri, params=params)
            if response.getcode() != 200:
                return {
                    'status': False,
                    'error': 'httpStatusCode(%d) != 200' % response.getcode(),
                }

            result = json.loads(response.read())
            if int(result['status']) == 200:
                return {
                    'status': True,
                    'live_token': result['data']['token'],
                    'live_open_id': result['data']['openId'],
                }

            if int(result['status']) == 500:
                err_result = 'message(%s)' % result['msg']
                i += 1
                time.sleep(waitTime)
                continue

            return {
                'status': False,
                'error': 'message(%s)' % result['msg'],
            }

        return {
            'status': False,
            'error': err_result,
        }

    @staticmethod
    def SuccessOrderByLiveOpenID(live_open_id, order_type, gold, money, expr, platform_type, order_id):
        nonce = genRandomString()
        params = {
            'nonce_str': nonce,
            'app_id': config().app_key,
            'uid': live_open_id,
            'request_id': genUniqueIDString(config().app_key),
            'type': str(order_type),
            'value': str(gold),
            'money': str(money),
            'expriation': str(time.mktime(datetime.now().timetuple()) + expr * 86400),
            'channel': config().alias,
            'platform': platform_type,
        }

        if len(order_id) > 0:
            params['order_id'] = order_id

        params['sign'] = genSign(params, config().app_secret)

        uri = config().url + '/open/finanv0/orderSuccess'

        err_result = ''
        i = 0
        while i < 3:

            response = http().post(uri=uri, params=params)

            if response.getcode() != 200:
                return {
                    'status': False,
                    'error': 'httpStatusCode(%d) != 200' % response.getcode(),
                }

            result = json.loads(response.read())
            if int(result['status']) == 200:
                return {
                    'status': True,
                    'golds': int(result['data']['livemeTokens']),
                }

            if int(result['status']) == 500:
                err_result = 'message(%s)' % result['msg']
                i += 1
                time.sleep(waitTime)
                continue

            return {
                'status': False,
                'error': 'message(%s)' % result['msg'],
            }

        return {
            'status': False,
            'error': err_result,
        }

    @staticmethod
    def ChangeGoldByLiveOpenID(live_open_id, order_type, gold, expr, optional_reason=''):
        print(genUniqueIDString(config().app_key))
        nonce = genRandomString()
        params = {
            'nonce_str': nonce,
            'app_id': config().app_key,
            'uid': live_open_id,
            'request_id': genUniqueIDString(config().app_key),
            'type': str(order_type),
            'value': str(gold),
        }
        if expr > 0:
            params['expriation'] = str(time.mktime(datetime.now().timetuple()) + expr * 86400)

        if len(optional_reason) > 0:
            params['reason'] = optional_reason

        params['sign'] = genSign(params, config().app_secret)

        uri = config().url + '/open/finanv0/changeGold'

        err_result = ''
        i = 0
        while i < 3:

            response = http().post(uri=uri, params=params)

            if response.getcode() != 200:
                return {
                    'status': False,
                    'error': 'httpStatusCode(%d) != 200' % response.getcode(),
                }

            result = json.loads(response.read())

            if int(result['status']) == 200:
                return {
                    'status': True,
                    'ok': True,
                }

            if int(result['status']) == 500:
                err_result = 'message(%s)' % result['msg']
                i += 1
                time.sleep(waitTime)
                continue

            return {
                'status': True,
                'ok': False,
                'msg': 'message(%s)' % result['msg'],
            }

        return {
            'status': False,
            'error': err_result,
        }

    @staticmethod
    def GetGoldByLiveOpenID(live_open_id):
        nonce = genRandomString()
        params = {
            'nonce_str': nonce,
            'app_id': config().app_key,
            'uid': live_open_id,
        }
        params['sign'] = genSign(params, config().app_secret)

        uri = config().url + '/open/finanv0/getUserTokens'

        err_result = ''
        i = 0
        while i < 3:

            response = http().get(uri=uri, params=params)

            if response.getcode() != 200:
                return {
                    'status': False,
                    'error': 'httpStatusCode(%d) != 200' % response.getcode(),
                }

            result = json.loads(response.read())
            if int(result['status']) == 200:
                return {
                    'status': True,
                    'golds': int(result['data']['livemeTokens']),
                }

            if int(result['status']) == 500:
                err_result = 'message(%s)' % result['msg']
                i += 1
                time.sleep(waitTime)
                continue

            return {
                'status': False,
                'error': 'message(%s)' % result['msg'],
            }

        return {
            'status': False,
            'error': err_result,
        }


class LvLIVE(Live):
    def __init__(self):
        Live.__init__(self)

    def GetTokenByThirdUID(self, third_uid, a_id, user_name='', sex=SexTypeUnknown, portrait_uri='', user_email='',
                           country_code='', birthday=''):
        return super(LvLIVE, self).GetTokenByThirdUID(third_uid, a_id, user_name, sex, portrait_uri, user_email,
                                                      country_code, birthday)

    def SuccessOrderByLiveOpenID(self, live_open_id, order_type, gold, money, expr, platform_type, order_id):
        return super(LvLIVE, self).SuccessOrderByLiveOpenID(live_open_id, order_type, gold, money, expr, platform_type,
                                                            order_id)

    def ChangeGoldByLiveOpenID(self, live_open_id, order_type, gold, expr, optional_reason=''):
        return super(LvLIVE, self).ChangeGoldByLiveOpenID(live_open_id, order_type, gold, expr, optional_reason)

    def GetGoldByLiveOpenID(self, live_open_id):
        return super(LvLIVE, self).GetGoldByLiveOpenID(live_open_id)


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
