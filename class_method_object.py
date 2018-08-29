# 方法对象
class Person :
    def __init__(self) :
        pass
    def run(self) : # 类方法的第一个参数必须是self
        print('跑啊跑', self)

p = Person()
p.run()
# 等价于
Person.run(p)

# 方法对象，可以单独存储起来，在需要的是有再调用
p_r = p.run
while True :
    p_r()
    break
