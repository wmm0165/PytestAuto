import pytest
from selenium import webdriver
from py._xmlgen import html

_driver = None


# 测试失败时添加截图和测试用例描述(用例的注释信息)

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)
    cells.pop()  # modify by linuxchao at 2018.0803 delete link for report


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)
    cells.pop()  # modify by linuxchao at 2018.0803 delete link for report


def _capture_screenshot():
    """
    截图保存为base64
    :return:
    """
    return _driver.get_screenshot_as_base64()


# 这里我设置的级别是模块级别，也就是每个测试文件运行一次
@pytest.fixture(scope='module')
def driver():
    global _driver
    print('------------open browser------------')
    # 启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # _driver = webdriver.Chrome("D:/soft/49chrome/Chrome/chromedriver.exe")  # 驱动chrome浏览器
    _driver = webdriver.Chrome(chrome_options=option)  # 驱动谷歌浏览器
    # _driver = webdriver.Firefox() # 驱动火狐浏览器
    _driver.maximize_window()
    yield _driver
    print('------------close browser------------')
    _driver.quit()
