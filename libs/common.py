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