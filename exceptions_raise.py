# 抛出异常
raise NameError('HiThere')

# 能抛出的异常，必须继承自Exception

# 可以直接抛出不带参数的异常，会用默认的构造函数来初始化错误
raise ValueError

# finally 子句不管会是否异常都执行的代码，值得注意的是finally不会截获异常，异常还是会正常抛出
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

# with 关键字可以在闭包执行完之后，执行清理的操作，如
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
