from . import admin_view,student_view,teacher_view
from libs import common

views_funcs = {
    "1": admin_view.view,
    "2": teacher_view.view,
    "3": student_view.view
}



msg = """
请选择视图:
    1. 管理员视图
    2. 老师视图
    3. 学生视图
"""

def run():
    common.select_func(views_funcs,msg)