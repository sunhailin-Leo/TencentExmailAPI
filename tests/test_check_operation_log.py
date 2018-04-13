# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : test_check_operation_check.py
"""

from tencent_exmail.SystemLog.CheckOperationLog import GetOperationLog

ACCESS_TOKEN = "abcd1234"


def test_op_log():
    op_log = GetOperationLog(access_token=ACCESS_TOKEN,
                             begin_date="2016-10-01",
                             end_date="2016-10-07",
                             operate_type=1)
    res = op_log.check()
    assert res
