"""
 把要存取的数据放到data目录下
 然后把各个人员用文件夹分开
 admin
 teacher
 student
"""
import os.path
import pickle
from conf import settings


"""
默认创建一个管理员对象
"""


def get_admin(user_name):
    """
    根据要获取的类型确定在哪一个文件夹
    拼接一个完整的路径路径存在就反序列化读取里面的内容
    不存在返回None
    :return:
    """
    path = os.path.join(settings.DATA_PATH, 'admin', user_name)
    if os.path.exists(path):
        with open(path,mode='rb') as f:
            res = pickle.load(f)
        return res

def save_obj(user_obj):
    """
    1.先拼接完整的路径,根据传入的user_obj来生成相应的数据存储目录。
    :param user_obj: 用户对象
    :return: bool
    """
    user_name =  user_obj.name
    userdata_save_dir = os.path.join(settings.DATA_PATH,user_obj.__class__.__name__.lower())
    # 判断下存储该用户的目录是否存在，不存在就创建
    if not os.path.exists(userdata_save_dir):
        os.mkdir(userdata_save_dir)

    # 把对象持久化
    userdata_save_path = os.path.join(userdata_save_dir,user_name)
    with open(userdata_save_path,mode='wb') as f:
        pickle.dump(user_obj,f)