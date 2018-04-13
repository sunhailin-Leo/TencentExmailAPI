# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : test_login_mail.py
"""
from tencent_exmail.Login.LoginMail import LoginTencentExmail


ACCESS_TOKEN = "abcd1234"


def test_login():
    log = LoginTencentExmail(access_token=ACCESS_TOKEN,
                             userid="123")
    res = log.login()
    assert res