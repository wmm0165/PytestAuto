
class ContactData(object):
    """添加联系人测试数据"""

    add_contact_success = [
        (
            "wangmmengmeng",
            "wangmm@ipharmacare.net",
            "1",
            "13691571234",
            "新建联系人1",
            "281754041@qq.com"
        )
    ]
    add_contact_fail = [
        (
            "linux2",
            "@qq.com",
            "0",
            "13691579842",
            "添加联系人2",
            "请正确填写邮件地址。"
        )
    ]


if __name__ == '__main__':
    pass
