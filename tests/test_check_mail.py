# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : test_check_mail.py
"""

from tencent_exmail.SystemLog.CheckMail import GetMailInfo

ACCESS_TOKEN = "abcd1234"


def test_check_mail():
    mail = GetMailInfo(access_token=ACCESS_TOKEN,
                       begin_date="2016-10-01",
                       end_date="2016-10-07",
                       mail_type=0,
                       userid="1234",
                       subject="test")
    res = mail.check()
    assert res
