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
    先选择学校，通过接口把学校列出
    根据用户选择确定的学校确认校区
    根据用户输入的老师名称确认老师名称
    """
    schools = admin_interface.get_school_interface()

    # 选择学校对象
    school = common.select_obj(schools, "校区")

    teacher_name = input("请输入老师的名字: ").strip()

    if teacher_name:
        t_create_res = admin_interface.create_teacher_interface(teacher_name,school)
        if t_create_res:
            print('老师创建成功.')
        else:
            print('老师已经存在请重试.')
    else:
        print('请输入正确的名称.')



def create_course():
    """
    2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开

    3. 课程包含，周期，价格，通过学校创建课程
   课程类对象
       属性:名字,价格,周期
       行为: 暂时无
    1.调用接口拿到校区
    2.根据用户号选择确认校区
    3.获取用户输入的课程信息
    4.调用接口保存课程信息
    :return:
    """
    pass

def select_course():
    """
    展示课程并选择一个正确的课程
    1.获取校区下的所有课程
    2.输入课程名称
    3.判定是否正确
        正确返回相应的课程名称
    :return:
    """
    pass


def create_class():
    """
    4. 通过学校创建班级， 班级关联课程、讲师
   班级对象
   属性:名字, 课程名称
   老师由管理管之后进行安排
    :return:
    """
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