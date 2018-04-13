# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : GroupManagement.py
"""

from tencent_exmail.BaseRequest.BaseHttpRequest import BaseHttpRequest

API_URL = "https://api.exmail.qq.com/cgi-bin/group/{}?access_token={}"


class Group:
    def __init__(self,
                 access_token,
                 operation: str,
                 groupid: str,
                 groupname='',
                 userlist='',
                 grouplist='',
                 department='',
                 allow_type=0,
                 allow_userlist=''):
        """
        邮件群组
        :param access_token: 调用接口凭证(必须)
        :param operation: 操作[创建、更新、删除、查询] (必须)
        :param groupid: 邮件群组名称 (创建(必须), 更新(必须))
        :param groupname: 邮件群组名称 (创建(必须), 更新)
        :param userlist: 成员帐号，userlist，grouplist，department至少一个。成员由userlist，grouplist，department共同组成
        :param grouplist: 成员邮件群组，userlist，grouplist，department至少一个。成员由userlist，grouplist，department共同组成
        :param department: 成员部门，userlist，grouplist，department至少一个。成员由userlist，grouplist，department共同组成
        :param allow_type: 群发权限。0: 企业成员, 1任何人， 2:组内成员，3:指定成员 (创建(必须)， 更新) --- 默认为0
        :param allow_userlist: 群发权限为指定成员时，需要指定成员
        """
        # 请求对象
        self._request = BaseHttpRequest()

        # 参数
        self._access_token = access_token
        self._operation = operation
        self._groupid = groupid
        self._groupname = groupname
        self._userlist = userlist
        self._grouplist = grouplist
        self._department = department
        self._allow_type = allow_type
        self._allow_userlist = allow_userlist

        if self._userlist != "" and not isinstance(self._userlist, list):
            raise TypeError("Userlist type is err!")

        if self._grouplist != "" and not isinstance(self._grouplist, list):
            raise TypeError("Grouplist type is err!")

        if self._allow_userlist != "" and not isinstance(self._allow_userlist, list):
            raise TypeError("Allow_userlist type is err!")

        # URL
        operation_list = ["create", "update", "delete", "get"]
        if operation in operation_list:
            self._api_url = API_URL.format(operation, self._access_token)
        else:
            raise ValueError("Operation is error!")

    def create_mail_group(self):
        """
        创建邮件群组
        :return:
        """
        if "create" in self._api_url:
            data = {
                "groupid": self._groupid,
                "groupname": self._groupname,
                "userlist": self._userlist,
                "department": self._department,
                "allow_type": self._allow_type,
                "allow_userlist": self._allow_userlist
            }
            res = self._request.request(method="POST", url=self._api_url, json=data)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def update_mail_group(self):
        """
        更新邮件群组
        :return:
        """
        if "update" in self._api_url:
            data = {
                "groupid": self._groupid,
                "groupname": self._groupname,
                "userlist": self._userlist,
                "department": self._department,
                "allow_type": self._allow_type,
                "allow_userlist": self._allow_userlist
            }
            res = self._request.request(method="POST",
                                        url=self._api_url,
                                        json=data)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def delete_mail_group(self):
        """
        删除邮件群组
        :return:
        """
        if "delete" in self._api_url:
            self._api_url = self._api_url + "&groupid=" + self._groupid
            res = self._request.request(method="GET",
                                        url=self._api_url)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def get_mail_group_info(self):
        """
        获取邮件群组信息
        :return:
        """
        if "get" in self._api_url:
            self._api_url = self._api_url + "&groupid=" + self._groupid
            res = self._request.request(method="GET",
                                        url=self._api_url)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}
