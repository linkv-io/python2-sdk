# -*- coding: UTF-8 -*-

import json
import hashlib
import time

from .tools import genGUID, getTimestampS, getTimestampMS
from .config import config
from linkv_sdk.http.http import http

waitTime = 0.3


class Im(object):
    def __init__(self):
        pass

    @staticmethod
    def getTokenByThirdUID(third_uid):

        nonce = genGUID()
        timestamp = getTimestampS()

        arr = [nonce, timestamp, config().app_secret]
        arr.sort()
        md5 = hashlib.new('md5')
        md5.update(''.join(arr).decode(encoding='utf8'))
        cmimToken = md5.hexdigest().lower()

        sha1 = hashlib.new('sha1')
        sha1.update('{}|{}|{}|{}'.format(config().app_id, config().app_key, timestamp, nonce).decode(encoding='utf8'))
        sign = sha1.hexdigest().upper()

        headers = {
            'nonce': nonce,
            'timestamp': timestamp,
            'cmimToken': cmimToken,
            'signature': cmimToken,
            'sign': sign,
            'appkey': config().app_key,
            'appUid': third_uid,
            'appId': config().app_id,
        }

        params = {
            'userId': third_uid,
        }
        uri = config().url + '/api/rest/getToken'

        err_result = ''
        i = 0
        while i < 3:
            response = http().post(uri=uri, params=params, headers=headers)

            if response.getcode() != 200:
                return {
                    'status': False,
                    'error': 'httpStatusCode(%d) != 200' % response.status,
                }

            result = json.loads(response.read())
            if int(result['code']) == 200:
                return {
                    'status': True,
                    'im_token': result['token'],
                }

            return {
                'status': False,
                'error': 'code not 200(%s)' % result['code'],
            }

        return {
            'status': False,
            'error': err_result,
        }

    @staticmethod
    def pushConverseData(from_uid, to_uid, object_name, content,
                         push_content='', push_data='', device_id='', to_app_id='',
                         to_user_ext_sys_user_id='', is_check_sensitive_words=''):

        nonce = genGUID()
        timestamp = getTimestampS()

        arr = [nonce, timestamp, config().app_secret]
        arr.sort()
        md5 = hashlib.new('md5')
        md5.update(''.join(arr).decode(encoding='utf8'))
        cmimToken = md5.hexdigest().lower()

        sha1 = hashlib.new('sha1')
        sha1.update('{}|{}|{}|{}'.format(config().app_id, config().app_key, timestamp, nonce).decode(encoding='utf8'))
        sign = sha1.hexdigest().upper()

        headers = {
            'nonce': nonce,
            'timestamp': timestamp,
            'cmimToken': cmimToken,
            'sign': sign,
            'appkey': config().app_key,
            'appId': config().app_id,
        }

        params = {
            'fromUserId': from_uid,
            'toUserId': to_uid,
            'objectName': object_name,
            'content': content,
            'appId': config().app_id,
        }

        if len(push_content) > 0:
            params['pushContent'] = push_content

        if len(push_data) > 0:
            params['pushData'] = push_data

        if len(device_id) > 0:
            params['deviceId'] = device_id

        if len(to_app_id) > 0:
            params['toUserAppid'] = to_app_id

        if len(to_user_ext_sys_user_id) > 0:
            params['toUserExtSysUserId'] = to_user_ext_sys_user_id

        if len(is_check_sensitive_words) > 0:
            params['isCheckSensitiveWords'] = is_check_sensitive_words

        uri = config().url + '/api/rest/message/converse/pushConverseData'

        err_result = ''
        i = 0
        while i < 3:
            response = http().post(uri=uri, params=params, headers=headers)

            if response.getcode() != 200:
                return {
                    'status': False,
                    'error': 'httpStatusCode(%d) != 200' % response.status,
                }

            result = json.loads(response.read())
            if int(result['code']) == 200:
                return {
                    'status': True,
                    'ok': True,
                }

            return {
                'status': False,
                'error': 'message(%s)' % result['msg'],
            }

        return {
            'status': False,
            'error': err_result,
        }


class LvIM(Im):
    def __init__(self):
        Im.__init__(self)

    def getTokenByThirdUID(self, third_uid):

        if len(third_uid) == 0:
            return {
                'status': False,
                'error': 'params error',
            }

        return super(LvIM, self).getTokenByThirdUID(third_uid)

    def pushConverseData(self, from_uid, to_uid, object_name, content,
                         push_content='', push_data='', device_id='', to_app_id='',
                         to_user_ext_sys_user_id='', is_check_sensitive_words=''):

        if len(from_uid) == 0 or len(to_uid) == 0 or len(object_name) == 0 or len(content) == 0:
            return {
                'status': False,
                'error': 'params error',
            }

        return super(LvIM, self).pushConverseData(from_uid, to_uid, object_name, content, push_content,
                                                  push_data, device_id, to_app_id, to_user_ext_sys_user_id,
                                                  is_check_sensitive_words)
