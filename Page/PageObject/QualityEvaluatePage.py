# -*- coding: utf-8 -*-
# @Time : 2019/9/11 10:32
# @Author : wangmengmeng

from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class QualityEvaluatePage(BasePage):
    do_conf = ParseConFile()
    new_project = do_conf.get_locators_or_account('PersonalQualityPageElements', 'new_project')
    extract_btn = do_conf.get_locators_or_account('PersonalQualityPageElements', 'extract_btn')
    save_btn = do_conf.get_locators_or_account('PersonalQualityPageElements', 'save_btn')
    generate_report = do_conf.get_locators_or_account('PersonalQualityPageElements', 'generate_report')
    project_names = do_conf.get_locators_or_account('PersonalQualityPageElements', 'project_names')
    savepro_name = do_conf.get_locators_or_account('PersonalQualityPageElements', 'savepro_name')
    savepro_confirm = do_conf.get_locators_or_account('PersonalQualityPageElements', 'savepro_confirm')
    view_report = do_conf.get_locators_or_account('PersonalQualityPageElements', 'view_report')
    export_btn = do_conf.get_locators_or_account('PersonalQualityPageElements', 'export_btn')
    download_btn = do_conf.get_locators_or_account('PersonalQualityPageElements', 'download_btn')

    def create_pro(self, projectname):
        # 点击新建评价项目
        self.click(*self.new_project)
        # 选择条件后进行抽取
        self.click(*self.extract_btn)
        # 保存项目
        self.click(*self.save_btn)
        # 生成报表
        self.click(*self.generate_report)
        # 填写项目名称
        self.send_keys(*self.savepro_name, projectname)
        # 点击确定
        self.click(*self.savepro_confirm)
        # 点击查看报表
        self.click(*self.view_report)
        # 点击导出
        self.click(*self.export_btn)
        # 点击下载
        self.click(*self.download_btn)

    def get_projectnames(self):
        """获取列表所有项目名称，由于没有处理翻页，这里只统计了第一页的数据"""
        names = self.find_elements(*self.project_names)
        return [ele.text for ele in names]

    def project_result(self, projecetname):
        """判断评价项目是否创建成功"""
        if projecetname in self.get_projectnames():
            return 'pass'
        else:
            return 'fail'

