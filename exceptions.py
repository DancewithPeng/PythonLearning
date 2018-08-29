# python中运行时的错误，称为异常

# 异常捕获
while True :
    try:
        x = int(input('请输入一个数字: '))
        print(f'您输入的数字为: {x}')
        break
    except ValueError :
        print('您输入了一个错误的数字，请重新输入')
    
# except 的字句可以同时处理多个错误，用元组表示
while True :
    try :
        x = int(input('请输入一个数字: '))
        break
    except (RuntimeError, TypeError, NameError, ValueError) :
        print('😂出错啦')
        break

