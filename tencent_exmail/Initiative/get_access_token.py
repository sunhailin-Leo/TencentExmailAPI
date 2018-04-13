# -*- coding: utf-8 -*-
"""
Create on: 2018-4-12
@Author  : sunhailin-Leo
@File    : get_access_token.py
"""

from tencent_exmail.BaseRequest.BaseHttpRequest import BaseHttpRequest

# 接口地址
API_URL = "https://api.exmail.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}"


class GetAccessToken:
    def __init__(self, corpid, corpsecret=None):
        """
        获取AccessToken
        :param corpid: 这个id是唯一的
        :param corpsecret: 这个secret是可以在管理后台刷新变更的
        """
        # 请求对象
        self._request = BaseHttpRequest()

        # 参数
        self._corpid = corpid
        self._corpsecret = corpsecret

        # Token
        self._access_token = ""

        # 构造访问链接
        if corpsecret is None:
            self._access_token = ""
        self._api_url = API_URL.format(corpid, corpsecret)

    def get_access_token(self):
        """
        获取AccessToken
        :return:
        """
        res = self._request.request(method="GET",
                                    url=self._api_url)
        # 返回码
        res_json = res.json()
        if res_json['errcode'] == 0:
            res_json.pop('errmsg')
            res_json.pop('errcode')
            return res_json
        else:
            return res.json()


