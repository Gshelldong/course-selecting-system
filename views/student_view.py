from libs import common


"""
根据需求文档创建功能
7.1 学员视图， 可以注册，登陆, 交学费， 选择班级,查看成绩
"""

def registry():
    pass

def login():
    pass

def pay_money():
    pass

def select_class():
    pass

def show_source():
    pass

funcs = {
    "1": registry,
    "2": login,
    "3": pay_money,
    "4": select_class,
    "5": show_source
}


msg = """
请选择学生功能:
    1. 注册
    2. 登陆
    3. 缴费
    4. 选择课程
    5. 查成绩
"""

def view():
    """
    展示学生所有功能。
    :return:
    """
    common.select_func(funcs,msg)