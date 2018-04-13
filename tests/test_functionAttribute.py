# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : test_functionAttribute.py
"""
from tencent_exmail.FunctionSetting.FunctionAttribute import Function


ACCESS_TOKEN = "abcd1234"


def test_get_function_attribute():
    func = Function(access_token=ACCESS_TOKEN,
                    operation="get",
                    userid="1234",
                    function_type=[1, 2, 3])
    res = func.get_function_attribute()
    assert res


def test_update_function_attribute():
    func = Function(access_token=ACCESS_TOKEN,
                    operation="update",
                    userid="1234",
                    option=[{"type": 1, "value": "0"},
                            {"type": 2, "value": "1"},
                            {"type": 3, "value": "0"}])
    res = func.update_function_attribute()
    assert res
