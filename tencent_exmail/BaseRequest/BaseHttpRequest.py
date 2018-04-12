# -*- coding: utf-8 -*-
"""
Create on: 2018-4-12
@Author  : sunhailin-Leo
@File    : BaseHttpRequest.py
"""

import requests


class BaseHttpRequest:
    def __init__(self):
        self._http = requests.Session()

    def request(self, method, url, **kwargs):
        """
        请求方法
        :param method: 方法
        :param url: 链接
        :param kwargs: 参数
        :return:
        """
        res = self._http.request(
            method=method,
            url=url,
            **kwargs
        )
        try:
            res.raise_for_status()
        except requests.RequestException as req_err:
            print(req_err)
        return res
