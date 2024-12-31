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
