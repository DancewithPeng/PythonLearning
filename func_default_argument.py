# 函数默认参数

def ask_ok(prompt, retries=4, reminder='Please try again!') :
    while True :
        ok = input(prompt) # input用户输入，参数是用户输入的提示参数
        if ok in ('y', 'ye', 'yes') :
            return True
        if ok in ('n', 'no', 'nop', 'nope') :
            return False

        retries -= 1
        if retries < 0 :
            raise ValueError('Vaind user response')
            
        print(reminder)

ask_ok('Do you really want to quit?')


# 默认参数可以是变量，但是取的是代码块定义时候的值，不会随着变量的改变而改变
i = 5
def f(arg=i) :
    print(arg)

i = 6
f()

# 默认参数只会赋值一次
def af(a, L=[]) :
    L.append(a)
    return L

print(af(1))
print(af(2))
print(af(3))

# 如果不想每次调用都共享默认参数，可以用以下的方式：
def af2(a, L=None) :
    if L is None :
        L = []
    L.append(a)
    return L

print(af2(1))
print(af2(2))
print(af2(3))

# 默认参数在调用时可以用keyword=value的形式
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(state='1234', voltage=100)

# 数组和字典, 参数如果市一个 * 号，表示传的是list，如果市两个 ** 号，表示传的市dict
def myFunc(arg1, *arg2, **arg3) :
    print(arg1)
    for a in arg2 :
        print(a)
    
    for k in arg3 :
        print(k, ':', arg3[k])

myFunc(1234, 'arr1', 'arr2', k1='kvalue1', k2='kvalue2', k3='kvalue3')