# 导入模块
import fibo

# 调用模块内的方法
print(fibo.fib(1000))
print(fibo.fib2(100))
print(fibo.__name__)

# 本地化模块名
fib = fibo.fib
print(fib(1000))