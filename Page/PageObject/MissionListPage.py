# -*- coding: utf-8 -*-
# @Time : 2019/9/7 10:43
# @Author : wangmengmeng
from Page.BasePage import BasePage
from util.parseConFile import ParseConFile
import time

class MissionListPage(BasePage):
    do_conf = ParseConFile()
    multi_box = do_conf.get_locators_or_account('MissionListPageElements', 'multi_box')
    first_box = do_conf.get_locators_or_account('MissionListPageElements', 'first_box')
    multi_btn = do_conf.get_locators_or_account('MissionListPageElements', 'multi_btn')
    multi_succMsg = do_conf.get_locators_or_account('MissionListPageElements', 'multi_succMsg')
    start_sf = do_conf.get_locators_or_account('MissionListPageElements', 'start_sf')
    end_sf = do_conf.get_locators_or_account('MissionListPageElements', 'end_sf')
    view = do_conf.get_locators_or_account('MissionListPageElements', 'view')
    aduit_advice = do_conf.get_locators_or_account('MissionListPageElements', 'audit_advice')
    reject_btn1 = do_conf.get_locators_or_account('MissionListPageElements', 'reject_btn1')
    reject_btn2 = do_conf.get_locators_or_account('MissionListPageElements', 'reject_btn2')
    pass_btn = do_conf.get_locators_or_account('MissionListPageElements', 'pass_btn')
    back_list = do_conf.get_locators_or_account('MissionListPageElements', 'back_list')

    def multi_one(self):
        """批量通过单个任务"""
        self.click_first_box()
        self.click_multi_btn()
        flag = self.is_element_exist(*self.multi_succMsg)
        assert flag

    # def multi_all(self):
        """批量通过待审列表全部任务"""

    def audit_reject1(self):
        """审核打回"""
        self.click_view()
        self.input_audit_advice()
        time.sleep(1)
        self.click_reject_btn1()
        self.click_back_list()

    def audit_reject2(self):
        """审核打回（可双签）"""
        self.click_view()
        self.input_audit_advice()
        time.sleep(1)
        self.click_reject_btn2()
        self.click_back_list()

    def audit_pass(self):
        """审核通过"""
        self.click_view()
        time.sleep(1)
        self.click_pass_btn()
        self.click_back_list()
    # def click_multi_box(self):
    #     self.click(self.multi_box)

    def click_first_box(self):
        self.click(*self.first_box)

    def click_multi_btn(self):
        self.click(*self.multi_btn)

    def click_start_sf(self):
        self.click(*self.start_sf)

    def click_end_sf(self):
        self.click(*self.end_sf)

    def click_view(self):
        self.click(*self.view)

    def input_audit_advice(self,audit_advice = "审核意见"):
        self.send_keys(*self.aduit_advice,audit_advice)

    def click_reject_btn1(self):
        self.click(*self.reject_btn1)

    def click_reject_btn2(self):
        self.click(*self.reject_btn2)

    def click_pass_btn(self):
        self.click(*self.pass_btn)

    def click_back_list(self):
        self.click(*self.back_list)

