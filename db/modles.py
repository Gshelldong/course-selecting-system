"""
模型其实就是对象。
就是专门存储数据的对象。
"""

class School:
    def __init__(self,name,address,):
        self.name = name
        self.address = address


class Course:
    def __init__(self,class_name,price,cycle,school_name):
        self.class_name = class_name
        self.price = price
        self.cycle = cycle
        self.school_name = school_name

class Classes:
    def __init__(self,name,course_name):
        self.name = name
        self.name = course_name
        self.teacher_name = None


class Teacher:
    def __init__(self,name,password,school_name):
        self.name = name
        self.password = password
        self.school_name = name
        self.class_name = None


class Student:
    def __init__(self,name,password,school_name,score):
        self.name = name
        self.password = password
        self.school_name = school_name
        self.class_name = None
        self.is_pay = False
        self.score = score

class Admin:
    def __init__(self,name,password):
        self.name = name
        self.password = password