"""
 把要存取的数据放到data目录下
 然后把各个人员用文件夹分开
 admin
 teacher
 student
"""
import os
import pickle
from conf import settings


"""
默认创建一个管理员对象
"""

# def get_admin(user_name):
#     """
#     根据要获取的类型确定在哪一个文件夹
#     拼接一个完整的路径路径存在就反序列化读取里面的内容
#     不存在返回None
#     :return:
#     """
#     path = os.path.join(settings.DATA_PATH, 'admin', user_name)
#     if os.path.exists(path):
#         with open(path,mode='rb') as f:
#             res = pickle.load(f)
#         return res

def save_obj(obj):
    """
    1.先拼接完整的路径,根据传入的user_obj来生成相应的数据存储目录。
    :param obj: 对象
    :return: bool
    """
    user_name =  obj.name
    userdata_save_dir = os.path.join(settings.DATA_PATH,obj.__class__.__name__.lower())
    # 判断下存储该用户的目录是否存在，不存在就创建
    if not os.path.exists(userdata_save_dir):
        os.mkdir(userdata_save_dir)

    # 把对象持久化
    userdata_save_path = os.path.join(userdata_save_dir,user_name)
    with open(userdata_save_path,mode='wb') as f:
        pickle.dump(obj,f)

def get_obj(cls_name,name):
    """
    根据类名称和对象的名称来获取一个对象。
    1.根据判断对象存储的路径判断有就获取.
    2..不存在返回None.
    :param cls_name:
    :param name:
    :return:
    """

    path = os.path.join(settings.DATA_PATH,cls_name,name)
    if os.path.exists(path):
        with open(path,mode='rb') as f:
            res = pickle.load(f)
        return res

def get_all(cls_name) -> list:
    """
    :param cls_name: 类的名称，要查看哪一类的所有对象
    :return: 返回的list是从类文件夹下面读取出来的对象名称
    会根据cls_name拼接读取对象的路径，这样获取的就是一类对象
    """
    obj_path = os.path.join(settings.DATA_PATH,cls_name)
    if not os.path.exists(obj_path):
        return False
    obj_names = os.listdir(obj_path)
    obj_lists = []
    for obj_name in obj_names:
        obj = get_obj(cls_name,obj_name)
        obj_lists.append(obj)
    return obj_lists

