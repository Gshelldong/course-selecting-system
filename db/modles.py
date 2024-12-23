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
    def __init__(self,class_name,price,cycle,school_name):
        self.class_name = class_name
        self.price = price
        self.cycle = cycle
        self.school_name = school_name

class Classes(BaseClass):
    def __init__(self,name,course_name):
        self.name = name
        self.name = course_name
        self.teacher_name = None


class Teacher(BaseClass):
    def __init__(self,name,school_name,password):
        self.name = name
        self.school_name = school_name
        self.password = password
        self.class_name = None


class Student(BaseClass):
    def __init__(self,name,password,school_name,score):
        self.name = name
        self.password = password
        self.school_name = school_name
        self.class_name = None
        self.is_pay = False
        self.score = score

class Admin(BaseClass):
    def __init__(self,name,password):
        self.name = name
        self.password = password