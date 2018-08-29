# 定义一个类
class MyClass :
    i = 1234
    
    def f(n) :
        print(n * 1234)

# 可以直接用类名.属性的方式，直接方位类属性
print(MyClass.i)

# 可以通过类名.方法的方式，返回方法函数
func = MyClass.f
func(10)

# 实例化
x = MyClass()
print(x)
print(x.i)

# 不能直接调用函数
# x.f(100)

# 初始化
class Person :
    def __init__(self, name, age) : # 初始化方法，第一个参数必须啊是self
        self.name = name
        self.age = age
        self.sex = 'man'

p = Person('zhangsan', 100)
print(p.name, p.age, p.sex)
