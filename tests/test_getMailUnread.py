# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : test_getMailUnread.py
"""
from tencent_exmail.NewMailNotification.GetMailUnread import GetUnreadMail


ACCESS_TOKEN = "abcd1234"


def test_get_unread_mail():
    get_unread = GetUnreadMail(access_token=ACCESS_TOKEN,
                               userid="1234")
    res = get_unread.get_unread_mails()
    assert res
