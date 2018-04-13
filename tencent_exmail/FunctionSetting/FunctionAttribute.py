# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : FunctionAttribute.py
"""

from tencent_exmail.BaseRequest.BaseHttpRequest import BaseHttpRequest

API_URL = "https://api.exmail.qq.com/cgi-bin/useroption/{}?access_token={}"


class Function:
    def __init__(self,
                 access_token: str,
                 operation: str,
                 userid: str,
                 function_type='',
                 option=''):
        """
        邮件功能设置
        :param access_token: 调用接口凭证 (必须)
        :param operation: 操作[获取、更改] (必须)
        :param userid: 成员UserID。企业邮帐号名，邮箱格式 (必须)
        :param function_type: 功能设置属性类型
                              1: 强制启用安全登录
                              2: IMAP/SMTP服务
                              3: POP/SMTP服务
                              4: 是否启用安全登录
                              (必须)
        :param option: 功能设置属性
                       type：属性类型。value:属性值（字符型）
                       示例: [{"type":1,"value":"0"},{"type":2,"value":"1"},{"type":3,"value":"0"}]}
                       1: 强制启用安全登录
                       2: IMAP/SMTP服务
                       3: POP/SMTP服务
                       4: 是否启用安全登录，不可用
                       (必须)
        """

        # 请求对象
        self._request = BaseHttpRequest()

        # 参数
        self._access_token = access_token
        self._operation = operation
        self._userid = userid
        self._function_type = function_type
        self._option = option

        if self._function_type != "" and not isinstance(self._function_type, list):
            raise TypeError("Function_type type is err!")

        if self._option != "" and not isinstance(self._option, list):
            raise TypeError("Option type is err!")

        # URL
        operation_list = ["get", "update"]
        if operation in operation_list:
            self._api_url = API_URL.format(operation, self._access_token)
        else:
            raise ValueError("Operation is error!")

    def get_function_attribute(self):
        """
        获取功能属性
        :return:
        """
        if "get" in self._api_url:
            data = {
                "userid": self._userid,
                "type": self._function_type
            }
            res = self._request.request(method="POST",
                                        url=self._api_url,
                                        json=data)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}

    def update_function_attribute(self):
        """
        更改功能属性
        :return:
        """
        if "update" in self._api_url:
            data = {
                "userid": self._userid,
                "option": self._option
            }
            res = self._request.request(method="POST",
                                        url=self._api_url,
                                        json=data)
            return res.json()
        else:
            return {'errmsg': 'Invalid input', 'errcode': -1}