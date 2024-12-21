from libs import common

"""
老师的功能
   7.2 讲师视图,登陆,(注册没有 由管理员来分配账号)， 查看班级学员列表 ， 修改所管理的学员的成绩 ,修改密码
"""

def login():
    pass

def show_class():
    pass

def show_students():
    pass


def modify_password():
    pass

def modify_source():
    pass

funcs = {
    "1": login,
    "2": show_class,
    "3": show_students,
    "4": modify_password,
    "5": modify_password
}

msg = """
请选择老师管理的功能:
    1. 登陆
    2. 查看班级
    3. 查看学员
    4. 修改密码
    5. 修改成绩
"""

def view():
    common.select_func(funcs,msg)