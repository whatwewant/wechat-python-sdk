# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from wechat_sdk.basic.crypto import BasicCrypto
from wechat_sdk.exceptions import NeedParamError
from wechat_sdk.utils import disable_urllib3_warning


class WechatConf(object):
    """ WechatConf 配置类

    该类将会存储所有和微信开发相关的配置信息, 同时也会维护配置信息的有效性.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs: 配置信息字典, 可用字典 key 值及对应解释如下:
                       'token': 微信 Token

                       'appid': App ID
                       'appsecret': App Secret

                       'encoding_aes_key': EncodingAESKey 值 (传入此值必须保证同时传入 token, appid, 否则抛出异常)

                       'access_token_getfunc': access token 获取函数 (用于分布式环境下, 具体格式参见文档, 无特殊需要则不需传入)
                       'access_token_setfunc': access token 写入函数 (用于分布式环境下, 具体格式参见文档, 无特殊需要则不需传入)
                       'access_token': 直接导入的 access token 值, 该值需要在上一次该类实例化之后手动进行缓存并在此处传入, 如果不
                                       传入, 将会在需要时自动重新获取 (传入 access_token_getfunc 和 access_token_setfunc 函数
                                       后将会自动忽略此处的传入值)
                       'access_token_expires_at': 直接导入的 access token 的过期日期, 该值需要在上一次该类实例化之后手动进行缓存
                                                  并在此处传入, 如果不传入, 将会在需要时自动重新获取 (传入 access_token_getfunc
                                                  和 access_token_setfunc 函数后将会自动忽略此处的传入值)

                       'jsapi_ticket_getfunc': jsapi ticket 获取函数 (用于分布式环境下, 具体格式参见文档, 无特殊需要则不需传入)
                       'jsapi_ticket_setfunc': jsapi ticket 写入函数 (用于分布式环境下, 具体格式参见文档, 无特殊需要则不需传入)
                       'jsapi_ticket': 直接导入的 jsapi ticket 值, 该值需要在上一次该类实例化之后手动进行缓存并在此处传入, 如果不
                                       传入, 将会在需要时自动重新获取 (传入 jsapi_ticket_getfunc 和 jsapi_ticket_setfunc 函数
                                       后将会自动忽略此处的传入值)
                       'jsapi_ticket_expires_at': 直接导入的 jsapi ticket 的过期日期, 该值需要在上一次该类实例化之后手动进行缓存
                                                  并在此处传入, 如果不传入, 将会在需要时自动重新获取 (传入 jsapi_ticket_getfunc
                                                  和 jsapi_ticket_setfunc 函数后将会自动忽略此处的传入值)

                       'partnerid': 财付通商户身份标识, 支付权限专用
                       'partnerkey': 财付通商户权限密钥 Key, 支付权限专用
                       'paysignkey': 商户签名密钥 Key, 支付权限专用

                       'checkssl': 是否检查 SSL, 默认不检查 (False), 可避免 urllib3 的 InsecurePlatformWarning 警告
        :return:
        """

        if kwargs.get('checkssl') is True:
            disable_urllib3_warning()  # 可解决 InsecurePlatformWarning 警告

        self.__token = kwargs.get('token')

        self.__appid = kwargs.get('appid')
        self.__appsecret = kwargs.get('appsecret')

        self.__encoding_aes_key = kwargs.get('encoding_aes_key')
        self.__crypto = None
        self._update_crypto()

        self.__access_token_getfunc = kwargs.get('access_token_getfunc')
        self.__access_token_setfunc = kwargs.get('access_token_setfunc')
        self.__access_token = kwargs.get('access_token')
        self.__access_token_expires_at = kwargs.get('access_token_expires_at')

        self.__jsapi_ticket_getfunc = kwargs.get('jsapi_ticket_getfunc')
        self.__jsapi_ticket_setfunc = kwargs.get('jsapi_ticket_setfunc')
        self.__jsapi_ticket = kwargs.get('jsapi_ticket')
        self.__jsapi_ticket_expires_at = kwargs.get('jsapi_ticket_expires_at')

        self.__partnerid = kwargs.get('partnerid')
        self.__partnerkey = kwargs.get('partnerkey')
        self.__paysignkey = kwargs.get('paysignkey')

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token):
        self.__token = token
        self._update_crypto()  # 改动 Token 需要重新更新 Crypto

    @property
    def appid(self):
        return self.__appid

    @appid.setter
    def appid(self, appid):
        self.__appid = appid
        self._update_crypto()  # 改动 App ID 需要重新更新 Crypto

    @property
    def appsecret(self):
        return self.__appsecret

    @appsecret.setter
    def appsecret(self, appsecret):
        self.__appsecret = appsecret

    @property
    def encoding_aes_key(self):
        return self.__encoding_aes_key

    @encoding_aes_key.setter
    def encoding_aes_key(self, encoding_aes_key):
        self.__encoding_aes_key = encoding_aes_key
        self._update_crypto()  # 改动 EncodingAESKey 需要重新更新 Crypto

    @property
    def crypto(self):
        return self.__crypto

    @property
    def access_token(self):
        if callable(self.__access_token_getfunc):
            return self.__access_token_getfunc()

        # TODO: 非分布式环境下的逻辑

    @access_token.setter
    def access_token(self, access_token):
        if callable(self.__access_token_setfunc):
            self.__access_token_setfunc(access_token)

        # TODO: 非分布式环境下的逻辑

    @property
    def jsapi_ticket(self):
        if callable(self.__jsapi_ticket_getfunc):
            return self.__jsapi_ticket_getfunc()

        # TODO: 非分布式环境下的逻辑

    @jsapi_ticket.setter
    def jsapi_ticket(self, jsapi_ticket):
        if callable(self.__jsapi_ticket_setfunc):
            self.__jsapi_ticket_setfunc(jsapi_ticket)

        # TODO: 非分布式环境下的逻辑

    @property
    def partnerid(self):
        return self.__partnerid

    @property
    def partnerkey(self):
        return self.__partnerkey

    @property
    def paysignkey(self):
        return self.__paysignkey

    def _update_crypto(self):
        """
        根据当前配置内容更新 Crypto 类
        """
        if self.__encoding_aes_key is not None:
            if self.__token is None or self.__appid is None:
                raise NeedParamError('Please provide token and appid parameters in the construction of class.')
            self.__crypto = BasicCrypto(self.__token, self.__encoding_aes_key, self.__appid)
        else:
            self.__crypto = None
