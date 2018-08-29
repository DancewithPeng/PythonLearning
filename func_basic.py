# 用 def 定义一个方法
def fib(n) :
    a, b = 0, 1
    while a < n :
        print(a, end=' ')
        a, b = b, a + b
    print()

fib(2000)

# 函数指针
f = fib
f(100)

fib(0)
print('不知道达到了什么')


# 返回值
def fib2(n) :
    result = []
    a, b = 0, 1
    while a < n : 
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)