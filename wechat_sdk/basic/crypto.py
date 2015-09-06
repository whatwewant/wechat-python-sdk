# -*- coding: utf-8 -*-

from wechat_sdk.lib.crypto import WechatBaseCrypto


class BasicCrypto(WechatBaseCrypto):
    """微信普通公众号(订阅/服务号)加密解密类"""

    def __init__(self, token, encoding_aes_key, app_id):
        super(BasicCrypto, self).__init__(token, encoding_aes_key, app_id)
        self.__app_id = app_id

    def encrypt_message(self, msg, nonce, timestamp=None):
        return self._encrypt_message(msg, nonce, timestamp)

    def decrypt_message(self, msg, msg_signature, timestamp, nonce):
        return self._decrypt_message(msg, msg_signature, timestamp, nonce)
