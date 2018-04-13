# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : test_userManagement.py
"""
from tencent_exmail.ContactManagement.UserManagement import User


ACCESS_TOKEN = "abcd1234"


def test_create_user():
    user = User(access_token=ACCESS_TOKEN,
                operation="create",
                userid="123@123.com",
                name="123",
                department=["1234"],
                position="test",
                mobile="13800138000",
                tel="12345678",
                extid="12",
                gender=1,
                slaves=["1234", "5678"],
                password="123456789",
                cpwd_login=1)
    res = user.create_user()
    assert res


def test_update_user():
    user = User(access_token=ACCESS_TOKEN,
                operation="update",
                userid="123@123.com",
                name="123",
                department=["1234"],
                position="test",
                mobile="13800138000",
                tel="12345678",
                extid="12",
                gender=1,
                slaves=["1234", "5678"],
                enable=1,
                password="123456789",
                cpwd_login=1)
    res = user.update_user()
    assert res


def test_delete_user():
    user = User(access_token=ACCESS_TOKEN,
                operation="delete",
                userid="1234")
    res = user.delete_user()
    assert res


def test_get_user():
    user = User(access_token=ACCESS_TOKEN,
                operation="get",
                userid="1234")
    res = user.get_user()
    assert res


def test_get_department_user():
    user = User(access_token=ACCESS_TOKEN,
                operation="simplelist",
                department_id="1234",
                fetch_child=0)
    res = user.get_department_user()
    assert res


def test_get_department_user_detail():
    user = User(access_token=ACCESS_TOKEN,
                operation="list",
                department_id="1234",
                fetch_child=0)
    res = user.get_department_user_detail()
    assert res


def test_batch_check_account():
    user = User(access_token=ACCESS_TOKEN,
                operation="batchcheck",
                userlist=["123", "234"])
    res = user.batch_check_account()
    assert res
