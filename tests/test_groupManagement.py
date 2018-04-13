# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : test_groupManagement.py
"""
from tencent_exmail.ContactManagement.GroupManagement import Group


ACCESS_TOKEN = "abcd1234"


def test_create_group():
    group = Group(access_token=ACCESS_TOKEN,
                  operation="create",
                  groupid="1234",
                  groupname="test",
                  userlist=["123", "234"],
                  department="1234",
                  allow_type=0,
                  allow_userlist=["1234", "234"])
    res = group.create_mail_group()
    assert res


def test_update_group():
    group = Group(access_token=ACCESS_TOKEN,
                  operation="update",
                  groupid="1234",
                  groupname="test",
                  userlist=["123", "234"],
                  department="1234",
                  allow_type=0,
                  allow_userlist=["1234", "234"])
    res = group.update_mail_group()
    assert res


def test_delete_group():
    group = Group(access_token=ACCESS_TOKEN,
                  operation="update",
                  groupid="1234")
    res = group.delete_mail_group()
    assert res


def test_get_mail_group_info():
    group = Group(access_token=ACCESS_TOKEN,
                  operation="get",
                  groupid="1234")
    res = group.get_mail_group_info()
    assert res
