from Page.BasePage import BasePage
from util.parseConFile import ParseConFile

import time


class HomePage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 首页
    # homePage = do_conf.get_locators_or_account('HomePageElements', 'homePage')
    # 通讯录
    # mailList = do_conf.get_locators_or_account('HomePageElements', 'mailList')
    # 应用中心
    # applicationCenter = do_conf.get_locators_or_account('HomePageElements', 'applicationCenter')
    # 收件箱
    # inBox = do_conf.get_locators_or_account('HomePageElements', 'inBox')
    wait = do_conf.get_locators_or_account('HomePageElements', 'wait')  # 待审任务
    wait_opt = do_conf.get_locators_or_account('HomePageElements', 'wait_opt')  # 待审门诊任务
    wait_ipt = do_conf.get_locators_or_account('HomePageElements', 'wait_ipt')  # 待审住院任务
    audit_setting = do_conf.get_locators_or_account('HomePageElements', 'audit_setting')  # 审方设置
    plan_setting = do_conf.get_locators_or_account('HomePageElements', 'plan_setting')  # 审方方案设置
    auth_setting = do_conf.get_locators_or_account('HomePageElements', 'auth_setting')  # 药师权限设置

    # def select_menu(self, menu='mailList'):
    def select_menu(self, menu):
        if menu == "plan_setting":
            time.sleep(2)
            self.click_audit_setting()
            self.click_plan_setting()
        elif menu == 'auth_setting':
            self.click_audit_setting()
            self.click_auth_setting()
        elif menu == 'wait_opt':
            time.sleep(2)
            self.click_wait()
            self.click_wait_opt()
        elif menu == 'wait_ipt':
            time.sleep(2)
            self.click_wait()
            self.click_wait_ipt()
        else:
            raise ValueError(
                '''菜单选择错误!
                plan_setting->审方方案设置
                auth_setting->药师权限设置
                '''
            )

    def click_audit_setting(self):
        return self.click(*HomePage.audit_setting)

    def click_plan_setting(self):
        return self.click(*HomePage.plan_setting)

    def click_auth_setting(self):
        return self.click(*HomePage.auth_setting)

    def click_wait(self):
        return self.click(*self.wait)

    def click_wait_opt(self):
        return self.click(*self.wait)

    def click_wait_ipt(self):
        return self.click(*self.wait)
    # def click_home_page_menu(self):
    #     return self.click(*HomePage.homePage)
    #
    # def click_address_list_menu(self):
    #     return self.click(*HomePage.mailList)
    #
    # def click_application_center_menu(self):
    #     return self.click(*HomePage.applicationCenter)
    #
    # def click_in_box_menu(self):
    #     return self.click(*HomePage.inBox)


if __name__ == '__main__':
    pass
