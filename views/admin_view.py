from libs import common
from interfaces import admin_interface

"""
管理视图，登陆,创建学校,创建讲师， 创建班级，创建课程,给老师指定班级
"""

def login():
    """
    输入用户名和密码
    通过接口进行判断
    接收接口的返回值
    :return:
    """
    username = input('请输入用户名: ')
    password = input('请输入密码:  ')
    if username and password:
        res = admin_interface.login(username, password)
        if res:
            print('登陆成功!')
        else:
            print('登陆失败!')
    else:
        print('请输入正确的用户名和密码.')

def create_school():
    pass

def create_teacher():
    pass

def select_course():
    pass

def create_course():
    pass


funcs = {
    "1": login,
    "2": create_school,
    "3": create_teacher,
    "4": select_course,
    "5": create_course
}

msg = ("""
请选择管理员功能:
    1. 登陆
    2. 创建学校
    3. 创建老师
    4. 选课
    5. 创建课程
""")
def view():
    common.select_func(funcs,msg)