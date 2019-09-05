# -*- coding: utf-8 -*-
# @Time : 2019/9/2 22:25
# @Author : wangmengmeng
from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class PlanSettingPage(BasePage):
    do_conf = ParseConFile()
    addplan_btn = do_conf.get_locators_or_account('PlanSettingPageElements', 'addplan_btn')
    save_btn = do_conf.get_locators_or_account('PlanSettingPageElements', 'save_btn')
    planname = do_conf.get_locators_or_account('PlanSettingPageElements', 'planname')

    def add_plan(self, planname):
        """新增审方方案流程"""
        self.click_addplan_btn()
        self.input_planname(planname)
        self.click_save_btn()

    def input_planname(self, planname):
        return self.send_keys(*PlanSettingPage.planname, planname)

    def click_addplan_btn(self):
        return self.click(*PlanSettingPage.addplan_btn)

    def click_save_btn(self):
        return self.click(*PlanSettingPage.save_btn)
