# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : test_batch_job.py
"""

from tencent_exmail.SystemLog.CheckBatchJob import GetBatchJobLog

ACCESS_TOKEN = "abcd1234"


def test_check_jobs():
    job = GetBatchJobLog(access_token=ACCESS_TOKEN,
                         begin_date="2016-10-01",
                         end_date="2016-10-07")
    res = job.check()
    assert res
