# -*- coding: utf-8 -*-
"""
Create on: 2018-5-20
@Author  : sunhailin-Leo
"""

# 成员管理

# 获取Token
from tencent_exmail.Initiative.get_access_token import GetAccessToken
from tencent_exmail.ContactManagement.UserManagement import User

# 公司ID
CORP_ID = "1234567"


# 成员管理只需要用到通讯录应用的secret
# 通讯录管理secret
CONTACT_SECRET = "abcdefghijklmnopqrstuvwxyz"


if __name__ == '__main__':
    # 获取AccessToken
    ex = GetAccessToken(corpid=CORP_ID, corpsecret=CONTACT_SECRET)
    res = ex.get_access_token()
    access_token = res['access_token']
    print(access_token)

    # 成员测试 --- 1 获取某个成员的信息
    user = User(access_token=access_token, operation="get", userid="xxx@yyy.com")
    res = user.get_user()
    # 返回是单个用户的json
    print(res)

    # 成员测试 --- 2 获取某个部门的成员(fetch_child为1即递归)
    user = User(access_token=access_token, operation="simplelist", department_id="123456", fetch_child=1)
    res = user.get_department_user()
    # 用户列表
    print(res['userlist'])

    # 成员测试 --- 3 获取某个部门的成员详情(fetch_child为1即递归)
    user = User(access_token=access_token, operation="list", department_id="123456", fetch_child=1)
    res = user.get_department_user_detail()
    # 用户列表
    print(res['userlist'])

    # 成员测试 --- 4 批量检查账号
    user = User(access_token=access_token, operation="batchcheck", userlist=["xxx@yyy.com"])
    res = user.batch_check_account()
    print(res['list'])

    # 成员测试 --- 5 删除成员
    user = User(access_token=access_token, operation="delete", userid="xxx@yyy.com")
    res = user.delete_user()
    print(res)

    # 成员创建、更新的基本结构都相同
    # 数据结构看源代码
