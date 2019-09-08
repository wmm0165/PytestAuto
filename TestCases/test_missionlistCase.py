# -*- coding: utf-8 -*-
# @Time : 2019/9/7 13:23
# @Author : wangmengmeng
import pytest


class TestMssionList:

    def test_multi_one(self, login, start_sf):
        """批量通过单个任务"""
        login[1].select_menu('wait_ipt')
        login[3].multi_one()

    def test_audit_reject1(self, login):
        """审核打回任务"""
        login[1].select_menu('wait_ipt')
        login[3].audit_reject1()

    def test_audit_reject2(self, login):
        """审核打回（可双签）任务"""
        login[1].select_menu('wait_ipt')
        login[3].audit_reject2()

    def test_audit_pass(self, login):
        """审核通过任务"""
        login[1].select_menu('wait_ipt')
        login[3].audit_pass()
    # def test_multi_all(self,login):
