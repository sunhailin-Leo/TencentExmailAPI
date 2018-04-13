# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : CheckMail.py
"""

from tencent_exmail.BaseRequest.BaseHttpRequest import BaseHttpRequest

API_URL = "https://api.exmail.qq.com/cgi-bin/log/mail?access_token={}"


class GetMailInfo:
    def __init__(self,
                 access_token,
                 begin_date,
                 end_date,
                 mail_type=0,
                 userid='',
                 subject=''):
        """
        查询邮件 https://exmail.qq.com/qy_mng_logic/doc#10028%20
        :param access_token: 调用接口凭证 (必须)
        :param begin_date: 开始日期。格式为2016-10-01 (必须)
        :param end_date: 结束日期。格式为2016-10-07 (必须)
        :param mail_type: 邮件类型。0:收信+发信 1:发信 2:收信 (必须) --- 默认为0
        :param userid: 筛选条件：指定成员帐号
        :param subject: 筛选条件：包含指定主题内容
        """
        # 请求对象
        self._request = BaseHttpRequest()

        # 参数
        self._access_token = access_token
        self._begin_date = begin_date
        self._end_date = end_date
        self._mail_type = mail_type
        self._userid = userid
        self._subject = subject

        # URL
        self._api_url = API_URL.format(self._access_token)

    def check(self):
        """
        查询邮件概况
        :return:
        """
        data = {
            "begin_date": self._begin_date,
            "end_date": self._end_date,
            "mailtype": self._mail_type,
            "userid": self._userid,
            "subject": self._subject
        }
        res = self._request.request(method="POST",
                                    url=self._api_url,
                                    json=data)
        return res.json()
