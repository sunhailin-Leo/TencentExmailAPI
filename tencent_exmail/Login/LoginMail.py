# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : LoginMail.py
"""

from tencent_exmail.BaseRequest.BaseHttpRequest import BaseHttpRequest

API_URL = "https://api.exmail.qq.com/cgi-bin/service/get_login_url?access_token={}&userid={}"


class LoginTencentExmail:
    def __init__(self,
                 access_token,
                 userid):
        """
        单点登陆 https://exmail.qq.com/qy_mng_logic/doc#10036%20
        :param access_token: 调用接口凭证 (必须)
        :param userid: 成员UserID (必须)
        """
        # 请求对象
        self._request = BaseHttpRequest()

        # 参数
        self._access_token = access_token
        self._userid = userid

        # URL
        self._api_url = API_URL.format(self._access_token, self._userid)

    def login(self):
        """
        登陆
        :return:
        """
        res = self._request.request(method="GET", url=self._api_url)
        return res.json()