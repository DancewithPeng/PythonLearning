# 参数注释
def my_func(x: int = 100, y: int = 200) -> int :
    print(my_func.__annotations__)
    return x + y

print(my_func())