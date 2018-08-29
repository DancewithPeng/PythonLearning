# 第二种导入模块名的方法，只导入用到的符号
from fibo import fib

fib(1000)

# 导入所有符号
from fibo import *
print(fib2(500))