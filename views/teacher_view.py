from libs import common
from interfaces import teacher_interface

"""
老师的功能
   7.2 讲师视图,登陆,(注册没有 由管理员来分配账号)， 查看班级学员列表 ， 修改所管理的学员的成绩 ,修改密码
"""

user_status = None

def login():
    username = input("请输入用户名: ").strip()
    password = input("请输入密码: ").strip()
    if username and password:
        res = teacher_interface.login_interface(username,password)
        if res:
            global user_status
            user_status = username
            print("登陆成功!")
        else:
            print("登陆失败!")
    else:
        print('请输入正确的用户名和密码!')

def show_class():
    teacher_name = user_status
    classes = teacher_interface.select_classes_interface(teacher_name)
    if not classes:
        print(f'{teacher_name}还没有分配班级')
    for class_team in classes:
        print(class_team)


def show_students():
    """
    1.展示登陆状态老师管理的班级，让老师选择班级
    2.展示该班级下所有的学生，然后选择学生
    3.根据选择的学生，调用interface打印学生的信息
    :return:
    """
    teacher = user_status
    classes = teacher_interface.get_class_interface(teacher)
    if not classes:
        print("请先给老师分配到班级!")
        return
    class_team = common.select_obj(classes,"班级名称")

    student_list = teacher_interface.select_student_interface(class_team)
    if not student_list:
        print("请先让学生注册!")
        return
    student = common.select_obj(student_list,"学生")

    student_obj = teacher_interface.get_student_detail_interface(student)
    print(f"""
    学生姓名：{student_obj.name}
    所在校区：{student_obj.school}
    所在班级：{student_obj.class_name}
    是否缴费：{student_obj.is_pay}
    学生成绩：{student_obj.score}""")

def modify_password():
    new_pas = input("请输入新密码: ").strip()
    chk_pas = input("请再次输入密码: ").strip()
    user_name = user_status
    if (new_pas is not None) and (new_pas == chk_pas):
        res = teacher_interface.modify_pas_interface(user_name,new_pas)
        if res:
            print("密码修改成功!")
        else:
            print("密码修改失败!")
    else:
        print("两次输入密码不一致!")

def modify_source():
    teacher = user_status
    classes = teacher_interface.get_class_interface(teacher)
    if not classes:
        print("请先给老师分配到班级!")
        return
    class_team = common.select_obj(classes,"班级名称")

    student_list = teacher_interface.select_student_interface(class_team)
    if not student_list:
        print("请先让学生注册!")
        return
    student = common.select_obj(student_list,"学生")

    source = input("请输入要修改的成绩: ").strip()
    if not source.isalnum():
        print("请输入正确的成绩!")
        return
    res = teacher_interface.modify_source_interface(student,source)
    if res:
        print("修改学生成绩成功!")
    else:
        print("修改失败")

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