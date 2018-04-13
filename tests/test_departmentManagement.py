# -*- coding: utf-8 -*-
"""
Create on: 2018-4-13
@Author  : sunhailin-Leo
@File    : test_departmentManagement.py
"""
from tencent_exmail.ContactManagement.DepartmentMangement import Department


ACCESS_TOKEN = "abcd1234"


def test_create_department():
    depart = Department(access_token=ACCESS_TOKEN,
                        operation="create",
                        depart_name="test",
                        depart_parent_id=1,
                        depart_order=0)
    res = depart.create_depart()
    assert res


def test_update_department():
    depart = Department(access_token=ACCESS_TOKEN,
                        operation="update",
                        depart_name="test",
                        depart_parent_id=1,
                        depart_order=0)
    res = depart.update_depart()
    assert res


def test_delete_depart():
    depart = Department(access_token=ACCESS_TOKEN,
                        operation="delete",
                        depart_id=1)
    res = depart.delete_depart()
    assert res


def test_search_depart():
    depart = Department(access_token=ACCESS_TOKEN,
                        operation="search",
                        depart_name="test",
                        depart_fuzzy=1)
    res = depart.search_departs()
    assert res

