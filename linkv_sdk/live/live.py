# -*- coding: UTF-8 -*-

import json
import time
from datetime import datetime

from .tools import genUniqueIDString, genRandomString, genSign
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
    def getTokenByThirdUID(third_uid, a_id, user_name='', sex=SexTypeUnknown, portrait_uri='', user_email='',
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
    def successOrderByLiveOpenID(live_open_id, order_type, gold, money, expr, platform_type, order_id):

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
                    'golds': int(result['data']['tokens']),
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
    def changeGoldByLiveOpenID(live_open_id, order_type, gold, expr, optional_reason=''):

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
    def getGoldByLiveOpenID(live_open_id):

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
                    'golds': int(result['data']['tokens']),
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

    def getTokenByThirdUID(self, third_uid, a_id, user_name='', sex=SexTypeUnknown, portrait_uri='', user_email='',
                           country_code='', birthday=''):

        if len(third_uid) == 0 or len(a_id) == 0:
            return {
                'status': False,
                'error': 'params error',
            }

        return super(LvLIVE, self).getTokenByThirdUID(third_uid, a_id, user_name, sex, portrait_uri, user_email,
                                                      country_code, birthday)

    def successOrderByLiveOpenID(self, live_open_id, order_type, gold, money, expr, platform_type, order_id):

        if len(live_open_id) == 0 or order_type == 0 or gold == 0 or money == 0 or expr == 0 or len(
                platform_type) == 0 or len(order_id) == 0:
            return {
                'status': False,
                'error': 'params error',
            }

        return super(LvLIVE, self).successOrderByLiveOpenID(live_open_id, order_type, gold, money, expr, platform_type,
                                                            order_id)

    def changeGoldByLiveOpenID(self, live_open_id, order_type, gold, expr, optional_reason=''):

        if len(live_open_id) == 0 or order_type == 0 or gold == 0 or expr == 0:
            return {
                'status': False,
                'error': 'params error',
            }

        return super(LvLIVE, self).changeGoldByLiveOpenID(live_open_id, order_type, gold, expr, optional_reason)

    def getGoldByLiveOpenID(self, live_open_id):

        if len(live_open_id) == 0:
            return {
                'status': False,
                'error': 'params error',
            }

        return super(LvLIVE, self).getGoldByLiveOpenID(live_open_id)
