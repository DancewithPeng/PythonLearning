# lambda 表达式，返回匿名函数
def make_incrementor(n) :
    return lambda x: x + n

f = make_incrementor(100)
print(f(0))
print(f(2))

def genrateResponse() :
    return lambda x, y : x * y

r = genrateResponse()
print(r(100, 200))

# 用户处理非常简单的逻辑
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key= lambda pair : pair[0])
print(pairs)