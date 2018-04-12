# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : CheckUserLogin.py
"""

from BaseRequest.BaseHttpRequest import BaseHttpRequest

API_URL = "https://api.exmail.qq.com/cgi-bin/log/login?access_token={}"


class GetUserLoginLog:
    def __init__(self,
                 access_token,
                 userid,
                 begin_date,
                 end_date):
        """
        查询成员登录 https://exmail.qq.com/qy_mng_logic/doc#10029%20
        :param access_token: 调用接口凭证 (必须)
        :param userid: 筛选条件：指定成员帐号 (必须)
        :param begin_date: 开始日期。格式为2016-10-01 (必须)
        :param end_date: 结束日期。格式为2016-10-07 (必须)
        """
        # 请求对象
        self._request = BaseHttpRequest()

        # 参数
        self._access_token = access_token
        self._userid = userid
        self._begin_date = begin_date
        self._end_date = end_date

        # URL
        self._api_url = API_URL.format(self._access_token)

    def check(self):
        """
        查询成员登录
        :return:
        """
        data = {
            "userid": self._userid,
            "begin_date": self._begin_date,
            "end_date": self._end_date,
        }
        res = self._request.request(method="POST",
                                    url=self._api_url,
                                    json=data)
        return res.json()
