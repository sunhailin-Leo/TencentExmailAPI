# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : test_check_mail_info.py
"""

from tencent_exmail.SystemLog.CheckMailInfo import ExMailInfo

ACCESS_TOKEN = "abcd1234"


def test_check_mail_info():
    mail_info = ExMailInfo(access_token=ACCESS_TOKEN,
                           domain="123@.com",
                           begin_date="2016-10-01",
                           end_date="2016-10-07")
    res = mail_info.check()
    assert res
