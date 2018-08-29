# 范围和命名空间
def scope_test() : 

    def do_local() :
        spam = 'local spam'  # 布局变量

    def do_nonlocal() :
        nonlocal spam  # 命名空间变量
        spam = 'nolocal spam'

    def do_global() :
        global spam # 全局变量
        spam = 'global spam' 

    spam = 'test spam'
    do_local()
    print('after local assignment:', spam)
    do_nonlocal()
    print('after nonlocal assignment:', spam)
    do_global()
    print('after global assignment:', spam)

scope_test()
print('in global scope: ', spam)