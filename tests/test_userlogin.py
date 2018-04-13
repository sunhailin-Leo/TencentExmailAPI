# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : test_userlogin.py
"""

from tencent_exmail.SystemLog.CheckUserLogin import GetUserLoginLog

ACCESS_TOKEN = "abcd1234"


def test_get_user_login_log():
    user_login_log = GetUserLoginLog(access_token=ACCESS_TOKEN,
                                     userid="1234",
                                     begin_date="2016-10-01",
                                     end_date="2016-10-07")
    res = user_login_log.check()
    assert res
