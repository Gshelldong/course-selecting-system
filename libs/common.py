import logging.config
from conf import settings


def select_func(funcs_dict,msg,callback=None):
    while True:
        print(msg)
        choice = input("(按q退出.) >>>: ")
        if choice == 'q':
            print("退出系统!")
            if callable(callback):
                callback()
            break
        if choice in funcs_dict:
            funcs_dict[choice]()
        else:
            print('请输入正确的选项.')

def select_obj(obj_name_list,obj_type):
    """
    这里传入一个类生成的所有对象的列表
    然后这个函数会处理成打印索引和元素
    给用户做选择并返回选择的元素
    :param schools:
    :return:
    """
    if not obj_name_list:
        print('请先创建%s!'%obj_type)
    else:
        print('编号 -> %s'%obj_type)
        for obj_name in obj_name_list:
            print(f'{obj_name_list.index(obj_name)} -> {obj_name}')

        choice = input('\n请选择%s编号: '%obj_type)
        if choice.isdigit():
            choice = int(choice)
            if choice in range(0,len(obj_name_list)+1):
                obj_name = obj_name_list[choice]
        return obj_name

def auth(auth_type):
    def auth_login(func):
        from views import admin_view,student_view,teacher_view
        def inner(*args,**kwargs):
            if auth_type == 'admin':
                module = admin_view
            elif auth_type == 'student':
                module = student_view
            elif auth_type == 'teacher':
                module = teacher_view
            else:
                raise "没有此认证类型!"

            if module.user_status:
                res = func(*args,**kwargs)
                return res
            else:
                print("请先登陆!")
                module.login()
        return inner
    return auth_login

def get_logger(log_name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(log_name)
    return logger