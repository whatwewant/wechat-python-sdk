# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import json
import unittest

import xmltodict
from httmock import urlmatch, HTTMock, response

from wechat_sdk.core.conf import WechatConf
from wechat_sdk.exceptions import NeedParamError


TESTS_PATH = os.path.abspath(os.path.dirname(__file__))
FIXTURE_PATH = os.path.join(TESTS_PATH, 'fixtures')


@urlmatch(netloc=r'(.*\.)?api\.weixin\.qq\.com$')
def wechat_api_mock(url, request):
    path = url.path.replace('/cgi-bin/', '').replace('/', '_')
    if path.startswith('_'):
        path = path[1:]
    res_file = os.path.join(FIXTURE_PATH, '%s.json' % path)
    content = {
        'errcode': 99999,
        'errmsg': 'can not find fixture %s' % res_file,
    }
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        with open(res_file, 'rb') as f:
            content = json.loads(f.read().decode('utf-8'))
    except (IOError, ValueError) as e:
        print(e)
    return response(200, content, headers, request=request)


class CoreConfTestCase(unittest.TestCase):
    token = 'test_token'
    appid = 'wx9354b770fe837911'
    appsecret = 'c994da14dca2047bb51caaedaf16f249'
    encoding_aes_key = 'ee5813b907f3e7f88b4561c5a59f6181304dc8e0bf9'

    fixtures_access_token = 'zHuVUpxuvAij5rZYpDTZbN1PaN0zQL9Op1mJy9Yex-qN7aNT0Wk5sSK3nEXv8FBmg6H' \
                            'bPwIuj-o5DR7nypN4BBkAk_CeZJVO7yUCgBPawsU'
    fixtures_jsapi_ticket = ''

    test_message = """<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>1348831860</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[测试信息]]></Content>
<MsgId>1234567890123456</MsgId>
</xml>"""

    def test_init_with_token(self):
        conf = WechatConf(token=self.token)
        self.assertEqual(conf.token, self.token)
        self.assertIsNone(conf.appid)
        self.assertIsNone(conf.appsecret)
        self.assertIsNone(conf.encoding_aes_key)
        self.assertIsNone(conf.crypto)

    def test_init_with_token_and_appid_appsecret(self):
        conf = WechatConf(token=self.token, appid=self.appid, appsecret=self.appsecret)
        self.assertEqual(conf.token, self.token)
        self.assertEqual(conf.appid, self.appid)
        self.assertEqual(conf.appsecret, self.appsecret)
        self.assertIsNone(conf.encoding_aes_key)
        self.assertIsNone(conf.crypto)

    def test_init_with_encoding_aes_key(self):
        conf = WechatConf(token=self.token, appid=self.appid, appsecret=self.appsecret,
                          encoding_aes_key=self.encoding_aes_key)
        self.assertEqual(conf.token, self.token)
        self.assertEqual(conf.appid, self.appid)
        self.assertEqual(conf.appsecret, self.appsecret)
        self.assertEqual(conf.encoding_aes_key, self.encoding_aes_key)
