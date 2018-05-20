# -*- coding: utf-8 -*-
"""
Create on: 2018-5-20
@Author  : sunhailin-Leo
"""

# 功能管理

# 获取Token
from tencent_exmail.Initiative.get_access_token import GetAccessToken
from tencent_exmail.FunctionSetting.FunctionAttribute import Function


# 公司ID
CORP_ID = "1234567"

# 功能管理只需要用到功能管理应用的secret
# 功能设置secret
FUNCTION_SETTING_SECRET = "abcdefghijklmnopqrstuvwxyz"

if __name__ == '__main__':
    # 获取AccessToken
    ex = GetAccessToken(corpid=CORP_ID, corpsecret=FUNCTION_SETTING_SECRET)
    res = ex.get_access_token()
    access_token = res['access_token']
    print(access_token)

    # 功能管理测试 --- 1 功能获取
    func = Function(access_token=access_token,
                    operation="get",
                    userid="xxx@yyy.com",
                    function_type=[1, 2, 3, 4])
    res = func.get_function_attribute()
    print(res['option'])

    # 功能管理测试 --- 2 修改功能
    func = Function(access_token=access_token,
                    operation="update",
                    userid="xxx@yyy.com",
                    option=[{"type": 1, "value": "0"},
                            {"type": 2, "value": "1"},
                            {"type": 3, "value": "0"},
                            {"type": 4, "value": "0"}])
    res = func.update_function_attribute()
    print(res)
