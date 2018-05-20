# -*- coding: utf-8 -*-
"""
Create on: 2018-5-20
@Author  : sunhailin-Leo
"""
# 获取邮件未读数

# 获取Token
from tencent_exmail.Initiative.get_access_token import GetAccessToken
from tencent_exmail.NewMailNotification.GetMailUnread import GetUnreadMail

# 公司ID
CORP_ID = "1234567"

# 新邮件提醒只需要用到新邮件提醒的secret
# 新邮件提醒secret
NEW_EMAIL_NOTIFICATION_SECRET = "abcdefghijklmnopqrstuvwxyz"


if __name__ == '__main__':
    # 获取AccessToken
    ex = GetAccessToken(corpid=CORP_ID, corpsecret=NEW_EMAIL_NOTIFICATION_SECRET)
    res = ex.get_access_token()
    access_token = res['access_token']
    print(access_token)

    # 获取邮件未读数
    email = GetUnreadMail(access_token=access_token, userid="xxx@yyy.com")
    res = email.get_unread_mails()
    print(res)
    # 数量
    print(res['count'])
