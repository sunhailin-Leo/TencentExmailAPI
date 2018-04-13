# -*- coding: utf-8 -*-
"""
Create on: 2018-4-12
@Author  : sunhailin-Leo
@File    : UserManagement.py
"""

from tencent_exmail.BaseRequest.BaseHttpRequest import BaseHttpRequest

API_URL = "https://api.exmail.qq.com/cgi-bin/user/{}?access_token={}"


class User:
    def __init__(self,
                 access_token,
                 operation,
                 userid='',
                 name='',
                 department='',
                 position='',
                 mobile='',
                 tel='',
                 extid='',
                 gender='',
                 slaves='',
                 enable=1,
                 password='',
                 cpwd_login='',
                 department_id='',
                 fetch_child=0,
                 userlist=''):
        """
        通讯录用户管理
        :param access_token: 调用接口凭证 (必须)
        :param operation: 操作 (必须) [创建、更新、删除、获取用户、获取部门用户、获取部门用户详情、批量检查账号]
        :param userid: 成员UserID。企业邮帐号名，邮箱格式 (创建(必须) , 更新(必须))
        :param name: 成员名称。长度为1~64个字节 (创建(必须) , 更新)
        :param department: 成员所属部门id列表，不超过20个 (创建(必须) , 更新)
        :param position: 职位信息。长度为0~64个字节 (创建, 更新)
        :param mobile: 手机号码 (创建, 更新)
        :param tel: 座机号码 (创建, 更新)
        :param extid: 编号 (创建, 更新)
        :param gender: 性别。1表示男性，2表示女性 (创建, 更新)
        :param slaves: 别名列表 1.Slaves 上限为5个 2.Slaves 为邮箱格式 (创建, 更新)
        :param enable: 启用/禁用成员。1表示启用成员，0表示禁用成员 (更新) --- 默认设置为1
        :param password: 密码 (创建(必须) , 更新)
        :param cpwd_login: 用户重新登录时是否重设密码, 登陆重设密码后，该标志位还原。0表示否，1表示是，缺省为0 (创建, 更新)
        :param department_id: 获取的部门id。id为1时可获取根部门下的成员 (获取(必须))
        :param fetch_child: 1/0：是否递归获取子部门下面的成员 (获取) --- 默认设置为0
        :param userlist: 成员帐号，每次检查不得超过20个
        """
        # 请求对象
        self._request = BaseHttpRequest()

        self._access_token = access_token
        self._operation = operation
        self._userid = userid
        self._name = name
        self._department = department
        self._position = position
        self._mobile = mobile
        self._tel = tel
        self._extid = extid
        self._gender = gender
        self._slaves = slaves
        self._enable = enable
        self._password = password
        self._cpwd_login = cpwd_login
        self._department_id = department_id
        self._fetch_child = fetch_child
        self._userlist = userlist

        if self._department != "" and not isinstance(self._department, list):
            raise TypeError("Department type is err!")

        if self._slaves != "" and not isinstance(self._slaves, list):
            raise TypeError("Slaves type is err!")

        if self._userlist != "" and not isinstance(self._userlist, list):
            raise TypeError("Userlist type is err!")

        # URL
        operation_list = ["create", "update", "delete", "get", "simplelist", "list", "batchcheck"]
        if operation in operation_list:
            self._api_url = API_URL.format(operation, self._access_token)
        else:
            raise ValueError("Operation is error!")

    def create_user(self):
        """
        创建成员
        :return:
        """
        if "create" in self._api_url:
            data = {
                "userid": self._userid,
                "name": self._name,
                "department": self._department,
                "position": self._position,
                "mobile": self._mobile,
                "tel": self._tel,
                "extid": self._extid,
                "gender": self._gender,
                "slaves": self._slaves,
                "password": self._password,
                "cpwd_login": self._cpwd_login
            }
            res = self._request.request(method="POST",
                                        url=self._api_url,
                                        json=data)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def update_user(self):
        """
        更新成员
        :return:
        """
        if "update" in self._api_url:
            data = {
                "userid": self._userid,
                "name": self._name,
                "department": self._department,
                "position": self._position,
                "mobile": self._mobile,
                "tel": self._tel,
                "extid": self._extid,
                "gender": self._gender,
                "slaves": self._slaves,
                "enable": self._enable,
                "password": self._password,
                "cpwd_login": self._cpwd_login
            }
            res = self._request.request(method="POST",
                                        url=self._api_url,
                                        json=data)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def delete_user(self):
        """
        删除用户
        :return:
        """
        if "delete" in self._api_url:
            self._api_url = self._api_url + "&userid=" + self._userid
            res = self._request.request(method="GET",
                                        url=self._api_url)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def get_user(self):
        """
        获取用户
        :return:
        """
        if "get" in self._api_url:
            self._api_url = self._api_url + "&userid=" + self._userid
            res = self._request.request(method="GET",
                                        url=self._api_url)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def get_department_user(self):
        """
        获取部门用户
        :return:
        """
        if "simplelist" in self._api_url:
            self._api_url = self._api_url + "&department_id=" + self._department_id\
                            + "&fetch_child=" + str(self._fetch_child)
            res = self._request.request(method="GET",
                                        url=self._api_url)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def get_department_user_detail(self):
        """
        获取部门用户（详情）
        :return:
        """
        if "list" in self._api_url:
            self._api_url = self._api_url + \
                            "&department_id=" + self._department_id + \
                            "&fetch_child=" + str(self._fetch_child)
            res = self._request.request(method="GET",
                                        url=self._api_url)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def batch_check_account(self):
        """
        批量检查账号
        :return:
        """
        if "batchcheck" in self._api_url:
            data = {"userlist": self._userlist}
            res = self._request.request(method="POST",
                                        url=self._api_url,
                                        json=data)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}
