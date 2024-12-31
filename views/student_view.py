from libs import common
from interfaces import student_interface

"""
根据需求文档创建功能
7.1 学员视图可以注册、登陆、交学费、选择班级、查看成绩
"""
user_status=None

def registry():
    username = input("请输入用户名: ").strip()
    password = input("请输入密码: ").strip()
    chk_password = input("请再次输入密码: ").strip()
    if password != chk_password:
        print("两次密码不一致")
        return

    schools = student_interface.get_school_interface()
    if not schools:
        print("还没有校区可以选择")
        return
    school = common.select_obj(schools, "校区")

    if username.isalpha() and (password != None):
        res = student_interface.regis_student_interface(username,password,school)
        if res:
            print("学生注册成功。")
        else:
            print("学员已经存在")
    else:
        print("请输入正确的用户名和密码")

def login():
    username = input("请输入用户名: ").strip()
    password = input("请输入密码: ").strip()
    global user_status

    if username and (password != None):
        res = student_interface.login_interface(username,password)
        if res:
            print("登陆成功")
            user_status = username
        else:
            print("登陆失败")
    else:
        print("请输入正确的用户名和密码")


def pay_money():
    global user_status
    user = user_status
    money = input("请输入缴纳的金额20000元: ").strip()
    if money.isalnum():
        money=int(money)
    else:
        print("输入错误!")
        return

    if money >= 20000:
        res,msg = student_interface.pay_money_interface(user)
        if res:
            print(msg)
        else:
            print(msg)
    else:
        print("请缴纳正确的金额.")

def select_class():
    pass

def select_source():
    pass

funcs = {
    "1": registry,
    "2": login,
    "3": pay_money,
    "4": select_class,
    "5": select_source
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