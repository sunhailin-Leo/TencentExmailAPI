# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : test_access_token.py
"""
from tencent_exmail.Initiative.get_access_token import GetAccessToken


CORPID = "abcd1234"
CORPSECRET = "abcd1234"


def test_get_access_token():
    access = GetAccessToken(corpid=CORPID,
                            corpsecret=CORPSECRET)
    token = access.get_access_token()
    assert token
