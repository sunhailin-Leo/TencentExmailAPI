# -*- coding: utf-8 -*-
"""
Create on: 2018-5-20
@Author  : sunhailin-Leo
"""

# 单点登录

# 获取Token
from tencent_exmail.Initiative.get_access_token import GetAccessToken
from tencent_exmail.Login.LoginMail import LoginTencentExmail

# 公司ID
CORP_ID = "1234567"

# 单点登陆secret
SINGE_LOGIN_SECRET = "abcdefghijklmnopqrstuvwxyz"

if __name__ == '__main__':
    # 获取AccessToken
    ex = GetAccessToken(corpid=CORP_ID, corpsecret=SINGE_LOGIN_SECRET)
    res = ex.get_access_token()
    access_token = res['access_token']
    print(access_token)

    # 单点登录测试
    login = LoginTencentExmail(access_token=access_token, userid="xxx@yyy.com")
    res = login.login()
    print(res)
    print("登录链接: %s" % res['login_url'])
