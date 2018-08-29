# 字面量格式化
import math
# 差值:后面表示格式
print(f'The value of pi is approximately {math.pi:.7f}.')

# 占位符，d表示空格在前面
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items() :
    print(f'{name:10} ==> {phone:10d}')

# !修饰符，表示在应用差值前对变量做修改，!a表示ascii()，!s表示str()，!r表示repr()
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals !r}.')