"""
模型其实就是对象。
就是专门存储数据的对象。

在对象中实现，对自己数据的存储和读取。
"""

from db import DBHander


class BaseClass:
    def save(self):
        DBHander.save_obj(self)

    @classmethod
    def get_obj(cls, name):
        # 这里的对象是从数据层的持久化文件中拿出来的
        return DBHander.get_obj(cls.__name__.lower(), name)

    @classmethod
    def get_all(cls):
        return DBHander.get_all(cls.__name__.lower())

class School(BaseClass):
    def __init__(self,name,address,):
        self.name = name
        self.address = address

class Course(BaseClass):
    def __init__(self,school,course_name,price,cycle):
        self.school = school
        self.name = course_name
        self.price = price
        self.cycle = cycle


class Classes(BaseClass):
    def __init__(self, name, school, course_name):
        self.name = name
        self.school = school
        self.course = course_name
        self.teacher_name = None


class Teacher(BaseClass):
    def __init__(self,name,school,password):
        self.name = name
        self.school = school
        self.password = password
        self.class_name = None

class Student(BaseClass):
    def __init__(self,name,password,school,score=0):
        self.name = name
        self.password = password
        self.school = school
        self.class_name = None
        self.is_pay = False
        self.score = score

class Admin(BaseClass):
    def __init__(self,name,password):
        self.name = name
        self.password = password