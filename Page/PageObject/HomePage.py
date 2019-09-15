from Page.BasePage import BasePage
from util.parseConFile import ParseConFile

import time


class HomePage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()

    wait = do_conf.get_locators_or_account('HomePageElements', 'wait')  # 待审任务
    wait_opt = do_conf.get_locators_or_account('HomePageElements', 'wait_opt')  # 待审门诊任务
    wait_ipt = do_conf.get_locators_or_account('HomePageElements', 'wait_ipt')  # 待审住院任务
    audit_review = do_conf.get_locators_or_account('HomePageElements', 'audit_review')  # 审核结果查看
    auditreview_opt = do_conf.get_locators_or_account('HomePageElements', 'auditreview_opt')  # 已审门诊处方查看
    auditreview_ipt = do_conf.get_locators_or_account('HomePageElements', 'auditreview_ipt')  # 已审住院医嘱查看
    message = do_conf.get_locators_or_account('HomePageElements', 'message')  # 警示信息管理
    message_list = do_conf.get_locators_or_account('HomePageElements', 'message_list')  # 用药警示管理
    statistic = do_conf.get_locators_or_account('HomePageElements', 'statistic')  # 审方工作分析
    quality_evaluate = do_conf.get_locators_or_account('HomePageElements', 'quality_evaluate')  # 审方质量评价
    personal_quality = do_conf.get_locators_or_account('HomePageElements', 'personal_quality')  # 评价结果查看
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
        elif menu == 'auditreview_opt':
            time.sleep(2)
            self.click(*self.audit_review)
            self.click(*self.auditreview_opt)
        elif menu == 'auditreview_ipt':
            time.sleep(2)
            self.click(*self.audit_review)
            self.click(*self.auditreview_ipt)
        elif menu == 'message_list':
            time.sleep(2)
            self.click(*self.message)
            self.click(*self.message_list)
        elif menu == 'quality_evaluate':
            time.sleep(2)
            self.click(*self.statistic)
            self.click(*self.quality_evaluate)
        elif menu == 'personal_quality':
            time.sleep(2)
            self.click(*self.personal_quality)
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


if __name__ == '__main__':
    pass
