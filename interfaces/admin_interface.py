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
    # admin_info = DBHander.get_admin(username)

    admin = modles.Admin.get_obj(username)

    if not admin:
        return False
    print(password)
    print(admin.password)
    if password == admin.password:
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

    admin = modles.Admin.get_obj(name)
    if admin:
        return "用户名已经存在."

    # 生成对象
    admin = modles.Admin(name,password)

    # 持久化对象
    admin.save()
    return ('注册成功.')


def create_school_interface(school_name,school_address):
    """
    创建学校的接口
    需要先判断学校是否存在，如果存在就返回false
    如果不存在就创建学校

    :param school_name: 学校的名称
    :param school_address: 学校的地址
    :return: bool
    """
    school = modles.School.get_obj(school_name) # 在modules中get_obj有两个实现参数，cls和name,因为使用类绑定方法cls已经被定义
                                                # 所以在这里只需要吧学校的名称传过去就好，返回的是布尔值或者是None。
    if school:
        # 有的话就不需要在创建对象了
        return False

    # 生成实例就持久化，把save()方法存放在modules 每个类的init方法中或者下面的方式
    school = modles.School(school_name,school_address)
    school.save()  # 写在这里方方便理解代码逻辑
    return True



# if __name__ == '__main__':
#     res = register_admin('admin','123')
#     print(res)
#
#     login_res = login('admin','123')
#     if login_res:
#         print('登陆成功')
#     else:
#         print('登陆失败')