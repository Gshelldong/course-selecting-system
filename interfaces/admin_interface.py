from db import DBHander


def login(username, password):
    """
    管理员登陆的接口
    传入用户名和密码
    :return: bool

    调用数据访问层获取用户的信息进行校验，校验是在接口层镜像校验
    数据层只负责返回数据。
    """
    admin_info = DBHander.get_admin(username)