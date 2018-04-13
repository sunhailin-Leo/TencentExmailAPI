# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : GetMailUnread.py
"""

from tencent_exmail.BaseRequest.BaseHttpRequest import BaseHttpRequest

# 主动模式
API_URL = "https://api.exmail.qq.com/cgi-bin/mail/newcount?access_token={}&userid={}"

# 回调模式
CALLBACK_MODE_API_URL = "http://api.3dept.com/?msg_signature={}&timestamp={}&nonce={}"


class GetUnreadMail:
    """
    主动模式
    """
    def __init__(self,
                 access_token,
                 userid):
        """
        获取邮件未读数 https://exmail.qq.com/qy_mng_logic/doc#10033%20 (官方文档有毛病...怀疑是实习生写的)
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

    def get_unread_mails(self):
        """
        获取邮件未读数
        :return:
        """
        res = self._request.request(method="GET", url=self._api_url)
        return res.json()


class CallBackGetUnreadMail:
    """
    回调模式（暂时不实现）
    """
    def __init__(self):
        pass

    def get_unread_mails(self):
        """
        获取邮件未读数(回调模式)
        :return:
        """
        pass

