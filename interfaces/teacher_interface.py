from db import modles

def login_interface(username,password):
    teacher = modles.Teacher.get_obj(username)
    if teacher:
        if teacher.name == username and teacher.password == password:
            return True


def select_classes_interface(teacher_name):
    teacher = modles.Teacher.get_obj(teacher_name)
    school = teacher.school

    class_list = []
    classes = modles.Classes.get_all()
    for class_team in classes: # type: modles.Classes
        # 如果这个班的校区和老师的校区相同且班级分配的老师和传入的老师一致就说明老师是管理该班级的老师
        if class_team.school == school and class_team.teacher_name == teacher.name:
            class_list.append(class_team.name)
    return class_list

def get_class_interface(teacher):
    classes = modles.Classes.get_all()
    class_list = []
    for class_team in classes:
        if class_team.teacher_name == teacher:
            class_list.append(class_team.name)
    return class_list

def select_student_interface(class_team):
    students = modles.Student.get_all()
    student_list = []
    for student in students: # type: modles.Student
        if student.class_name == class_team:
            student_list.append(student.name)
    return student_list


def get_student_detail_interface(student):
    student_obj = modles.Student.get_obj(student)
    return student_obj

def modify_pas_interface(user_name,password):
    teacher = modles.Teacher.get_obj(user_name)
    teacher.password = password
    teacher.save()
    return True

# TODO
def modify_source_interface(student,source):
    pass