def select_func(funcs_dict,msg):
    while True:
        print(msg)
        choice = input("(按q退出.) >>>: ")
        if choice == 'q':
            print("退出系统!")
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