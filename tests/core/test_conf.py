# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import json
import time
import unittest

import xmltodict
from httmock import urlmatch, HTTMock, response

from wechat_sdk.core.conf import WechatConf
from wechat_sdk.exceptions import NeedParamError
from tests.utils import api_weixin_mock


class CoreConfTestCase(unittest.TestCase):
    token = 'test_token'
    appid = 'wx9354b770fe837911'
    appsecret = 'c994da14dca2047bb51caaedaf16f249'
    encoding_aes_key = 'ee5813b907f3e7f88b4561c5a59f6181304dc8e0bf9'

    fixtures_access_token = 'HoVFaIslbrofqJgkR0Svcx2d4za0RJKa3H6A_NjzhBbm96Wtg_a3ifU' \
                            'YQvOfJmV76QTcCpNubcsnOLmDopu2hjWfFeQSCE4c8QrsxwE_N3w'
    fixtures_jsapi_ticket = 'bxLdikRXVbTPdHSM05e5u5sUoXNKd8-41ZO3MhKoyN5OfkWITDGgnr2' \
                            'fwJ0m9E8NYzWKVZvdVtaUgWvsdshFKA'

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
        with self.assertRaises(NeedParamError):
            getattr(conf, 'access_token')
        with self.assertRaises(NeedParamError):
            getattr(conf, 'jsapi_ticket')

    def test_init_with_token_and_appid_appsecret(self):
        conf = WechatConf(token=self.token, appid=self.appid, appsecret=self.appsecret)
        self.assertEqual(conf.token, self.token)
        self.assertEqual(conf.appid, self.appid)
        self.assertEqual(conf.appsecret, self.appsecret)
        self.assertIsNone(conf.encoding_aes_key)
        self.assertIsNone(conf.crypto)
        with HTTMock(api_weixin_mock):
            access_token = conf.access_token
            access_token_expires_at = int(time.time()) + 7200
            self.assertEqual(access_token, self.fixtures_access_token)
            self.assertEqual(conf._WechatConf__access_token, self.fixtures_access_token)
            self.assertIn(conf._WechatConf__access_token_expires_at, [access_token_expires_at-1,
                                                                      access_token_expires_at,
                                                                      access_token_expires_at+1])
            jsapi_ticket = conf.jsapi_ticket
            jsapi_ticket_expires_at = int(time.time()) + 7200
            self.assertEqual(jsapi_ticket, self.fixtures_jsapi_ticket)
            self.assertEqual(conf._WechatConf__jsapi_ticket, self.fixtures_jsapi_ticket)
            self.assertIn(conf._WechatConf__access_token_expires_at, [jsapi_ticket_expires_at-1,
                                                                      jsapi_ticket_expires_at,
                                                                      jsapi_ticket_expires_at+1])

    def test_init_with_encoding_aes_key(self):
        conf = WechatConf(token=self.token, appid=self.appid, appsecret=self.appsecret,
                          encoding_aes_key=self.encoding_aes_key)
        self.assertEqual(conf.token, self.token)
        self.assertEqual(conf.appid, self.appid)
        self.assertEqual(conf.appsecret, self.appsecret)
        self.assertEqual(conf.encoding_aes_key, self.encoding_aes_key)
