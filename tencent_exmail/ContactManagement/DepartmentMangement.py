# -*- coding: utf-8 -*-
"""
Create on: 2018-4-12
@Author  : sunhailin-Leo
@File    : DepartmentManagement.py
"""

from tencent_exmail.BaseRequest.BaseHttpRequest import BaseHttpRequest

API_URL = "https://api.exmail.qq.com/cgi-bin/department/{}?access_token={}"


class Department:
    def __init__(self,
                 access_token,
                 operation,
                 depart_id='',
                 depart_name='',
                 depart_parent_id='',
                 depart_order=0,
                 depart_fuzzy=0):
        """
        部门对象
        :param access_token: AccessToken调用接口凭证 (必须)
        :param operation: 操作变量(["create", "update", "delete", "list", "search"], 对应增、更、删、列、查)
        :param depart_id: 部门id (必须) (更新, 删除（注：不能删除根部门；不能删除含有子部门、成员的部门）, 获取列表)
        :param depart_name: 部门名称。长度限制为1~64个字节，字符不能包括\:*?"<>｜ (必须) (创建, 更新, 查找)
                            注: 更新时则为需要更新的名称
        :param depart_parent_id: 父部门id。id为1可表示根部门 (必须) (创建, 更新)
        :param depart_order: 在父部门中的次序值。order值小的排序靠前，1-10000为保留值，若使用保留值，将被强制重置为0。 (非必须) (创建, 更新)
        :param depart_fuzzy: 1/0：是否模糊匹配 (非必需) (查找)
        """
        # 请求对象
        self._request = BaseHttpRequest()

        # 参数
        self._access_token = access_token
        self._depart_id = depart_id
        self._depart_name = depart_name
        self._depart_parent_id = depart_parent_id
        self._depart_order = depart_order
        self._depart_fuzzy = depart_fuzzy

        # URL
        operation_list = ["create", "update", "delete", "list", "search"]
        if operation in operation_list:
            self._api_url = API_URL.format(operation, self._access_token)
        else:
            raise ValueError("Operation is error!")

    def create_depart(self):
        """
        创建部门
        :return:
        """
        # 封装参数
        if "create" in self._api_url:
            data = {'name': self._depart_name,
                    'parentid': self._depart_parent_id,
                    'order': self._depart_order}
            res = self._request.request(method="POST",
                                        url=self._api_url,
                                        json=data)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def update_depart(self):
        """
        更新部门
        :return:
        """
        # 封装参数
        if "update" in self._api_url:
            data = {"id": self._depart_id,
                    "name": self._depart_name,
                    "parentid": self._depart_parent_id,
                    "order": self._depart_order}
            res = self._request.request(method="POST",
                                        url=self._api_url,
                                        json=data)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def delete_depart(self):
        """
        删除部门
        :return:
        """
        if "delete" in self._api_url:
            self._api_url = self._api_url + "&id=" + str(self._depart_id)
            res = self._request.request(method="GET", url=self._api_url)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def list_departs(self):
        """
        获取部门列表
        :return:
        """
        if "list" in self._api_url:
            self._api_url = self._api_url + "&id=" + self._depart_id
            res = self._request.request(method="GET", url=self._api_url)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def search_departs(self):
        """
        查找部门
        :return:
        """
        if "search" in self._api_url:
            data = {"name": self._depart_name,
                    "fuzzy": self._depart_fuzzy}
            res = self._request.request(method="POST",
                                        url=self._api_url,
                                        json=data)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}
