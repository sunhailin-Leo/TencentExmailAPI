# -*- coding: utf-8 -*-
"""
Create on: 2018-5-20
@Author  : sunhailin-Leo
"""

# 成员管理

# 获取Token
from tencent_exmail.Initiative.get_access_token import GetAccessToken
from tencent_exmail.ContactManagement.GroupManagement import Group

# 公司ID
CORP_ID = "1234567"


# 邮件群组管理只需要用到通讯录应用的secret
# 通讯录管理secret
CONTACT_SECRET = "abcdefghijklmnopqrstuvwxyz"


if __name__ == '__main__':
    # 获取AccessToken
    ex = GetAccessToken(corpid=CORP_ID, corpsecret=CONTACT_SECRET)
    res = ex.get_access_token()
    access_token = res['access_token']
    print(access_token)

    # 邮件群组测试 --- 1
    group = Group(access_token=access_token, operation="delete", groupid="123456")
    res = group.delete_mail_group()
    print(res)

    # 邮件群组测试 --- 2
    group = Group(access_token=access_token, operation="get", groupid="123456")
    res = group.get_mail_group_info()
    print(res)

    # 邮件群组创建和更新需要传递参数过多，详情请看源代码
