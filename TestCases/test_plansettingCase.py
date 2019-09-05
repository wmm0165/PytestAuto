# -*- coding: utf-8 -*-
# @Time : 2019/9/5 15:04
# @Author : wangmengmeng
import pytest
# from data.plan_data import PlanData


class TestPlan:
    # plan_data = PlanData()

    @pytest.mark.parametrize('planname', ["ceshicesh17"])
    def test_addplan_success(self, login, planname):
        """添加审方方案"""
        home_page = login[1]
        plan_setting_page = login[2]
        home_page.select_menu('plan_setting')
        plan_setting_page.add_plan(planname)




