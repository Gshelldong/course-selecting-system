import sys,os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from views import main_view

"""
1.在ide中开发项目的时候，会自动吧项目的根目录加入到环境变量中，
但是在终端中执行的时候就不会有项目的根目录的环境变量而导致导入
项目依赖的时候报错。

2.如果在项目文件目录下执行的时候获取到的目录就是文件本身，导致dirname为空
无法加入到环境变量的情况，所以在最内层使用绝对路径的方式就可以完全的避免掉。

3.环境变量的添加应该添加在导入项目内部模块的之前。
"""


if __name__ == '__main__':
    main_view.run()