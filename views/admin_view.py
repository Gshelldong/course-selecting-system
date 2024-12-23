from libs import common
from interfaces import admin_interface

"""
管理视图,登陆,创建学校,创建讲师,创建班级,创建课程,给老师指定班级
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
    """
    用户输入学校的名称和地址
    调用接口进行创建
    接收返回值
    展示结果
    :return:
    """
    school_name = input("请输入学校名称: ").strip()
    school_address = input("请输入学校地址: ").strip()

    if school_address and school_name:
        res = admin_interface.create_school_interface(school_name,school_address)
        if res:
            print('学校创建成功.')
        else:
            print('学校已经创建.')
    else:
        print("请输入正确的学校名称和地址.")

def create_teacher():
    """
    6. 创建讲师角色时要关联学校
    """
    schools = admin_interface.get_school_interface()

    # 选择学校对象
    school = common.select_obj(schools, "校区")

    teacher_name = input("请输入老师的名字: ")

    if teacher_name:
        t_create_res = admin_interface.create_teacher_interface(teacher_name,school)
        if t_create_res:
            print('老师创建成功.')
        else:
            print('老师已经存在请重试.')
    else:
        print('请输入正确的名称.')








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