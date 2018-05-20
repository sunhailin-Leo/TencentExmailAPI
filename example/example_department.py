# -*- coding: utf-8 -*-
"""
Create on: 2018-5-20
@Author  : sunhailin-Leo
"""

# 部门管理

# 获取Token
from tencent_exmail.Initiative.get_access_token import GetAccessToken
from tencent_exmail.ContactManagement.DepartmentMangement import Department

# 公司ID
CORP_ID = "1234567"


# 部门管理只需要用到通讯录应用的secret
# 通讯录管理secret
CONTACT_SECRET = "abcdefghijklmnopqrstuvwxyz"


if __name__ == '__main__':
    # 获取AccessToken
    ex = GetAccessToken(corpid=CORP_ID, corpsecret=CONTACT_SECRET)
    res = ex.get_access_token()
    access_token = res['access_token']
    print(access_token)

    # 部门测试 --- 1 模糊查找部门名称含有IT或者为IT的部门信息
    department = Department(access_token=access_token, operation="search", depart_name="IT", depart_fuzzy=1)
    res = department.search_departs()
    print(res)

    # 部门测试 --- 2 查询某个部门ID下的下属部门信息
    department = Department(access_token=access_token, operation="list", depart_id="123456")
    res = department.list_departs()
    print(res)

    # 部门测试 --- 3 在某个部门下创建一个部门
    department = Department(access_token=access_token,
                            operation="create",
                            depart_name="xxx",
                            depart_parent_id="123456",
                            depart_order=1)
    res = department.create_depart()
    print(res)

    # 部门测试 --- 4 更新某个部门
    department = Department(access_token=access_token,
                            operation="update",
                            depart_id="789012",
                            depart_name="xxx",
                            depart_parent_id="123456",
                            depart_order=1)
    res = department.update_depart()
    print(res)

    # 部门测试 --- 5 删除某个部门 （注：不能删除根部门；不能删除含有子部门、成员的部门）
    department = Department(access_token=access_token,
                            operation="delete",
                            depart_id="123456")
    res = department.delete_depart()
    print(res)
