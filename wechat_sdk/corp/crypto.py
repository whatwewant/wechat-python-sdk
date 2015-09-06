# -*- coding: utf-8 -*-

from wechat_sdk.lib.crypto import WechatBaseCrypto


class CorpCrypto(WechatBaseCrypto):
    """微信企业号加密解密类"""

    def __init__(self, token, encoding_aes_key, corp_id):
        super(CorpCrypto, self).__init__(token, encoding_aes_key, corp_id)
        self.__corp_id = corp_id

    def check_signature(self, msg_signature, timestamp, nonce, echostr):
        return self._check_signature(msg_signature, timestamp, nonce, echostr)

    def encrypt_message(self, msg, nonce, timestamp=None):
        return self._encrypt_message(msg, nonce, timestamp)

    def decrypt_message(self, msg, msg_signature, timestamp, nonce):
        return self._decrypt_message(msg, msg_signature, timestamp, nonce)
