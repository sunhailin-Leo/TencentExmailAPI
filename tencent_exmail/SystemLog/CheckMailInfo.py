# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : CheckMailInfo.py
"""

from tencent_exmail.BaseRequest.BaseHttpRequest import BaseHttpRequest

API_URL = "https://api.exmail.qq.com/cgi-bin/log/mailstatus?access_token={}"


class ExMailInfo:
    def __init__(self,
                 access_token,
                 domain: str,
                 begin_date,
                 end_date):
        """
        查询邮件概况 https://exmail.qq.com/qy_mng_logic/doc#10027%20
        查询开始和结束时间有限制(3个月)
        :param access_token: 调用接口凭证(必须)
        :param domain: 域名(必须)
        :param begin_date: 开始日期。格式为2016-10-01(必须)
        :param end_date: 结束日期。格式为2016-10-07(必须)
        """
        # 请求对象
        self._request = BaseHttpRequest()

        # 参数
        self._access_token = access_token
        self._domain = domain
        self._begin_date = begin_date
        self._end_date = end_date

        # URL
        self._api_url = API_URL.format(self._access_token)

    def check(self):
        """
        查询邮件概况
        :return:
        """
        data = {
            "domain": self._domain,
            "begin_date": self._begin_date,
            "end_date": self._end_date
        }
        res = self._request.request(method="POST",
                                    url=self._api_url,
                                    json=data)
        return res.json()
