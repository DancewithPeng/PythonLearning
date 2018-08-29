# 继承
class Person :

    def __init__(self, name = '', age = 0) :
        self.name = name
        self.age = age
        self._pri_peroperty = 1234 # 
        self.__pro_preoperty = 2345 # 双下滑线是会自动添加类名，如： _Person__pro_preoperty

    def say_hi(self) :
        print(f'Hello, my name is {self.name}, {self.age} years old! {self._pri_peroperty}, {self.__pro_preoperty}')

# 继承自Person
class Student(Person) :

    def __init__(self, name = '', age = 0, class_numebr = 0, identifier = '') :
        self.class_number = class_numebr
        self.identifier = identifier

    def say_hi(self) :
        print(f'Hello, my name is {self.name}, {self.age} years old! my class numebr is {self.class_number}, and my identifier is {self.identifier}, {self._pri_peroperty}, {self.__pro_preoperty}')

class Teacher(Person) :
    
    def __init__(self, teacher_id = '') :
        self.teacher_id = teacher_id

    def say_hi(self) :
        print(f'Hello, I am teacher, my teacher id is {self.teacher_id}')        

# 多继承
class MyClass(Student, Teacher) :

    def __init__(self) :
        self.property = ''
    
    def say_hi(self) :
        print(f'哈哈哈哈，my property is {self.property}')

p = Person()
p.name = 'zhangpeng'
p.age = 18
p.say_hi()

s = Student()
s.name = 'zhangsan'
s.age = 100
s.class_number = 10
s.identifier = '0123456'
s._pri_peroperty = '1234'
s._Student__pro_preoperty = '1234'
s.say_hi()
    
t = Teacher()
t.teacher_id = '1234'
t.say_hi()

c = MyClass()
c.property = '1234'
c.teacher_id = '1234'
c.say_hi()