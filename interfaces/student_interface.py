from db import modles

def get_school_interface():
    schools = modles.School.get_all()
    school_list = []
    for school in schools:
        school_list.append(school.name)
    return school_list

def regis_student_interface(username,password,school):
    student = modles.Student.get_obj(username)
    if student:
        return False
    student = modles.Student(username,password,school)
    student.save()
    return True

def login_interface(username,password):
    user = modles.Student.get_obj(username) # type: modles.Student
    if not user:
        return False

    if user.name == username and user.password == password:
        return True


def pay_money_interface(user):
    user = modles.Student.get_obj(user) # type: modles.Student
    if user.is_pay:
        return False,'该用户已经缴费.'

    user.is_pay = True
    user.save()
    return True,"缴费成功."

def get_classes_interface(user):
    students = modles.Student.get_obj(user)
    classes = modles.Classes.get_all()
    class_list = []
    for class_team in classes:
        if class_team.school == students.school:
            class_list.append(class_team.name)
    return class_list


def select_class_interface(user, class_team):
    student = modles.Student.get_obj(user)
    if student.class_name != None:
        return False
    student.class_name == class_team
    student.save()
    return True

def select_score_interface(user):
    student = modles.Student.get_obj(user)
    source = student.score
