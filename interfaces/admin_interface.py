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


def get_school_interface() -> list:
    """
    获取到所有校区的名字
    :return: list
    """
    schools_list = []
    schools = modles.School.get_all()

    for school in schools:
        schools_list.append(school.name)
    return  schools_list


def create_teacher_interface(teacher_name,school,password='123'):
    teacher = modles.Teacher.get_obj(teacher_name)
    if teacher:
        # 如果存在老师的话就不创建了
        return False
    teacher = modles.Teacher(teacher_name,school,password)
    teacher.save()
    return True


def create_course_interface(school,course_name,course_price,course_cycle):
    course_name = school + "_" + course_name
    course = modles.Course.get_obj(course_name)
    if course:
        return False
    course = modles.Course(school,course_name,course_price,course_cycle)
    course.save()
    return True


def get_course_interface(school) -> list:
    """
    获取到每个每个校区的课程列表
    根据用户选择的校区进行返回相应的
    校区列表
    :return: list
    """
    courses_list = []
    courses = modles.Course.get_all()
    for course in courses:
        if school == course.school_name:
            courses_list.append(course.name)
    return courses_list


def create_class_interface(class_name,school,course):
    class_team = modles.Classes.get_obj(class_name)
    if class_team:
        return False
    class_team = modles.Classes(class_name,school,course)
    class_team.save()
    return True


def get_teacher_interface(school):
    teachers = modles.Teacher.get_all()
    teacher_list = []
    for teacher in teachers:
        if teacher.school == school:
            teacher_list.append(teacher.name)
    return teacher_list

def get_course_interface(school):
    courses = modles.Course.get_all()
    course_list = []
    for course in courses:
        if course.school == school:
            course_list.append(course.name)
    return course_list


def get_class_interface(school):
    classes = modles.Classes.get_all()
    class_list = []
    for class_team in classes:
        if class_team.school == school:
            class_list.append(class_team.name)
    return class_list

def t_share_course_interface(school,teacher_name,course,class_team):
    """
    要实现：
    老师在哪个班级上课
    班级设置是哪个老师在管理
    :return:
    """
    teacher = modles.Teacher.get_obj(teacher_name)
    if teacher.class_name == class_team:
        return False,"该班级已经存在该老师%s"%teacher_name
    teacher.class_name = class_team
    teacher.save()

    class_t = modles.Classes.get_obj(class_team)  # type: modles.Classes
    if class_t.teacher_name == teacher_name:
        return False,"该课程已经分配到该老师%s"%teacher_name
    class_t.teacher_name = teacher_name
    class_t.save()
    return True,'分配老师到班级课程成功!'


# 调试管理员的接口
# if __name__ == '__main__':
#     res = register_admin('admin','123')
#     print(res)
#
#     login_res = login('admin','123')
#     if login_res:
#         print('登陆成功')
#     else:
#         print('登陆失败')