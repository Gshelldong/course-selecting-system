from db import DBHander
from db import modles


def login(username, password):
    """
    管理员登陆的接口
    传入用户名和密码
    :return: bool

    调用数据访问层获取用户的信息进行校验，校验是在接口层镜像校验
    数据层只负责返回数据。
    """
    admin_info = DBHander.get_admin(username)

    if not admin_info:
        return False
    if password == admin_info.password:
        return True


def register_admin(name, password):
    """
    先通过名字获取管理员，如果存在则认为管理员重复了
    不存在就创建新的管理员
    最后保存这个对象
    :param name:
    :param password:
    :return:
    """

    obj = DBHander.get_admin(name)
    if obj:
        return "用户名已经存在."

    # 生成对象
    admin = modles.Admin(name,password)

    # 持久化对象
    DBHander.save_obj(admin)
    return ('注册成功.')


# if __name__ == '__main__':
#     res = register_admin('admin','123')
#     print(res)
#
#     login_res = login('admin','123')
#     if login_res:
#         print('登陆成功')
#     else:
#         print('登陆失败')