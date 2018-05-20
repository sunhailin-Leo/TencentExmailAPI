# -*- coding: utf-8 -*-
"""
Create on: 2018-5-20
@Author  : sunhailin-Leo
"""

# 系统日志

# 获取Token
from tencent_exmail.Initiative.get_access_token import GetAccessToken

from tencent_exmail.SystemLog.CheckMailInfo import ExMailInfo
from tencent_exmail.SystemLog.CheckMail import GetMailInfo
from tencent_exmail.SystemLog.CheckUserLogin import GetUserLoginLog
from tencent_exmail.SystemLog.CheckBatchJob import GetBatchJobLog
from tencent_exmail.SystemLog.CheckOperationLog import GetOperationLog

# 公司ID
CORP_ID = "1234567"

# 日志查询secret
LOG_SEARCH_SECRET = "abcdefghijklmnopqrstuvwxyz"

if __name__ == '__main__':
    # 获取AccessToken
    ex = GetAccessToken(corpid=CORP_ID, corpsecret=LOG_SEARCH_SECRET)
    res = ex.get_access_token()
    access_token = res['access_token']
    print(access_token)

    # 日志查询测试 --- 1 查询邮件概况
    # 查询时间有时间上限 （3个月）
    mail_status = ExMailInfo(access_token=access_token,
                             domain="yyy.com",
                             begin_date="2018-02-18",
                             end_date="2018-05-20")
    res = mail_status.check()
    print(res)
    if res["errcode"] != 601002:
        print("发信总量: %s 封" % res['sendsum'])
        print("收信总量: %s 封" % res['recvsum'])
    else:
        print("日志查询时间超过上限")

    # 日志查询测试 --- 2 查询收发邮件测试
    user_mail = GetMailInfo(access_token=access_token, begin_date="2018-02-18", end_date="2018-05-20")
    res = user_mail.check()
    [print(msg) for msg in res['list']]

    # 日志查询测试 --- 3 查询登录日志
    user_login_log = GetUserLoginLog(access_token=access_token,
                                     begin_date="2018-02-18",
                                     end_date="2018-05-20",
                                     userid='xxx@yyy.com')
    res = user_login_log.check()
    [print(msg) for msg in res['list']]
    """
    数据中有个type表示登录类型
    1：网页登录
    2：手机登录
    3：QQ邮箱App登录
    4：客户端登录:包括imap,pop,exchange
    5：其他登录方式
    """

    # 日志查询测试 --- 4 批量任务日志查询
    batch_job = GetBatchJobLog(access_token=access_token, begin_date="2018-02-18", end_date="2018-05-20")
    res = batch_job.check()
    [print(msg) for msg in res['list']]
    """
    操作类型
    1：群发邮件
    2：批量导入成员
    3：删除公告
    4：批量添加别名
    5：发布公告
    6：RTX帐号关联
    7：设置企业签名档
    8：取消企业签名档
    9：开通成员
    0：其他
    """

    # 日志查询测试 --- 5 查询操作记录
    op_log = GetOperationLog(access_token=access_token, begin_date="2018-02-18", end_date="2018-05-20", operate_type=0)
    res = op_log.check()
    [print(msg) for msg in res['list']]

    """
    参数	说明
    errcode	返回码
    errmsg	对返回码的文本描述内容
    list	列表数据
    time	时间（时间戳格式）
    operator	操作人员
    type	登录类型
    1：登录
    2：修改密码
    3：添加域名
    4：注销域名
    5：设置LOGO
    6：删除LOGO
    7：修改密保邮箱
    8：修改管理员邮箱
    9：发表公告
    10：群发邮件
    11：新增黑名单
    12：删除黑名单
    13：清空黑名单
    14：新增白名单
    15：删除白名单
    16：清空白名单
    17：新增域白名单
    18：删除域白名单
    19：新增用户
    20：删除用户
    21：启用用户
    22：禁用用户
    23：编辑用户
    24：编辑别名
    25：批量导入用户
    26：添加分级管理员
    27：删除分级管理员
    28：新增部门
    29：删除部门
    30：编辑部门
    31：移动部门
    32：新增邮件组
    33：删除邮件组
    34：编辑邮件组
    35：设置邮件备份
    36：邮件转移
    37：IP登录权限
    38：限制成员外发
    39：开启接口
    40：重新获取KEY
    41：停用接口
    operand	关联数据
    remark	备注信息：
    若type=20, remark=1表示帐号已还原
    """
