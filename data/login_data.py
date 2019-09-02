class LoginData(object):
    """用户登录测试数据"""

    login_success_data = [
        (
            "admin",
            "123456",
            "系统管理员"
        )
    ]

    login_fail_data = [
        (
            "linuxxiaochao",
            "",
            "请输入密码"
        ),
        (
            "",
            "xiaochao11520",
            "请输入帐号"
        ),
        (
            "linux",
            "xiaochao",
            "帐号或密码错误"
        )
    ]


# if __name__ == '__main__':
#     pass
