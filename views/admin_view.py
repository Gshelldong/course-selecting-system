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
        res = admin_interface.create_school_interface(school_name, school_address)
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
        t_create_res = admin_interface.create_teacher_interface(teacher_name, school)
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
    2.根据用户选择确认校区
    3.获取用户输入的课程信息
    4.调用接口保存课程信息
    :return:
    """
    schools = admin_interface.get_school_interface()
    school = common.select_obj(schools, "校区")
    if not school: return

    course_name = input("请输入想要创建的课程名称: ").strip()
    course_price = input("请输入想要创建的课程价格: ").strip()
    course_cycle = input("请输入想要创建的课程周期: ").strip()
    if course_name:
        course = admin_interface.create_course_interface(school, course_name, course_price, course_cycle)
        if course:
            print("课程创建成功.")
        else:
            print("课程已经存在.")
    else:
        print('请输入正确的课程名称！')


def create_class():
    """
    4. 通过学校创建班级,班级关联课程、讲师
    班级对象
    属性:名字,课程名称
    老师由管理管之后进行安排
    :return:
    """
    schools = admin_interface.get_school_interface()
    school = common.select_obj(schools, "校区")
    if not school: return

    courses = admin_interface.get_course_interface(school)
    course = common.select_obj(courses, "课程")
    if not course: return

    class_name = input("请输入班级名称: ").strip()
    if class_name:
        class_team = admin_interface.create_class_interface(class_name, school, course)
        if class_team:
            print("班级创建成功.")
        else:
            print("班级已经存在.")
    else:
        print("请输入正确的班级名称.")


def select_course():
    """
    要实现：
    老师在哪个班级上课
    班级设置是哪个老师在管理

    展示课程并选择一个正确的课程
    1.选择要管理哪个校区的老师
    2.选择要管理的老师
    3.老师分配的课程
    4.老师分配的班级
    5.判定老师是否分配在这个班级
    6.将老师、课程、班级提交给接口
         判断返回结果
    :return:
    """
    schools = admin_interface.get_school_interface()
    school = common.select_obj(schools, "学校")
    if not school: return

    teachers = admin_interface.get_teacher_interface(school)
    teacher = common.select_obj(teachers, "老师")
    if not teacher: return

    courses = admin_interface.get_course_interface(school)
    course = common.select_obj(courses, "课程")
    if not course: return

    classes = admin_interface.get_class_interface(school)
    class_team = common.select_obj(classes, "班级")
    if not class_team: return

    teacher_share_course, msg = admin_interface.t_share_course_interface(school, teacher, course, class_team)
    if teacher_share_course:
        print(msg)
    else:
        print(msg)


funcs = {
    "1": login,
    "2": create_school,
    "3": create_teacher,
    "4": create_course,
    "5": select_course,
    "6": create_class
}

msg = ("""
请选择管理员功能:
    1. 登陆
    2. 创建学校
    3. 创建老师
    4. 创建课程
    5. 分配课程
    6. 创建班级
""")


def view():
    common.select_func(funcs, msg)
