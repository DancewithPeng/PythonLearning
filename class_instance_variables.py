class Dog :
    kind = '🐶'   # 类属性
    def __init__(self, name) :
        self.name = name # 成员属性

d1 = Dog('aaa')
d2 = Dog('bbb')

print(d1.kind, d1.name, d2.kind, d2.name)

# 方法名可以定义在类外部
def hi(self, msg) :
    print(self, msg)

class Person :
    h = hi

p = Person()

# 这两个调用完全等价
hi(p, '你好')
p.h('😂😂😂')

# self可以调用其他实例方法
class Bag :

    def __init__(self) :
        self.data = []

    def add(self, x) : 
        self.data.append(x)

    def addtwice(self, x) :
        self.add(x)
        self.add(x)

