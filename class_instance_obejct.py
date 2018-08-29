# python中的实例对象

class Person :
    
    def __init__(self) :
        self.height = 185.0

p = Person()
print(p.height)

# python中的成员变量是可以运行时动态添加的
p.age = 100
print(p.age)

p.age += 200
print(p.age)

# 也可以动态删除对象的成员变量
del p.age
print(p.age)

