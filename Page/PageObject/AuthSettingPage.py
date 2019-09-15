# -*- coding: utf-8 -*-
# @Time : 2019/9/14 14:57
# @Author : wangmengmeng
from Page.BasePage import BasePage
from util.parseConFile import ParseConFile
from selenium.webdriver.common.action_chains import ActionChains


class AuthSettingPage(BasePage):
    do_conf = ParseConFile()
    add_btn = do_conf.get_locators_or_account('AuthSettingPageElements', 'add_btn')
    pharname = do_conf.get_locators_or_account('AuthSettingPageElements', 'pharname')
    pharname_first = do_conf.get_locators_or_account('AuthSettingPageElements', 'pharname_first')
    edit = do_conf.get_locators_or_account('AuthSettingPageElements', 'edit')
    delete = do_conf.get_locators_or_account('AuthSettingPageElements', 'delete')

    def click_add_btn(self):
        return self.click(*self.add_btn)

    def click_pharname(self):
        return self.click(*self.pharname)

    def click_pharname_first(self):
        return self.click(*self.pharname_first)

    def click_delete(self):
        return self.click(*self.delete)
