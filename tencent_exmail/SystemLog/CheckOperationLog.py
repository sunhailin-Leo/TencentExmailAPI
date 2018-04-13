# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : CheckOperationLog.py
"""

from tencent_exmail.BaseRequest.BaseHttpRequest import BaseHttpRequest

API_URL = "https://api.exmail.qq.com/cgi-bin/log/operation?access_token={}"


class GetOperationLog:
    def __init__(self,
                 access_token,
                 begin_date,
                 end_date,
                 operate_type=1):
        """
        查询操作记录
        :param access_token: 调用接口凭证
        :param operate_type: 类型
                                1：all
                                2：开放协议同步
                                3：编辑管理员帐号
                                4：设置分级管理员
                                5：编辑企业信息
                                6：收信黑名单设置
                                7：邮件转移设置
                                8：成员与群组管理
                                9：邮件备份管理
                                10：成员权限控制
        :param begin_date: 开始日期。格式为2016-10-01
        :param end_date: 结束日期。格式为2016-10-07
        """
        # 请求对象
        self._request = BaseHttpRequest()

        # 参数
        self._access_token = access_token
        self._operation_type = operate_type
        self._begin_date = begin_date
        self._end_date = end_date

        # URL
        self._api_url = API_URL.format(self._access_token)

    def check(self):
        """
        查询操作记录
        :return:
        """
        data = {
            "type": self._operation_type,
            "begin_date": self._begin_date,
            "end_date": self._end_date,
        }
        res = self._request.request(method="POST",
                                    url=self._api_url,
                                    json=data)
        return res.json()
