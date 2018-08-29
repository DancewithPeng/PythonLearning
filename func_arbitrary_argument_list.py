# 可变参数
def joinArgs(*args, sep='/') :
    return sep.join(args)

str = joinArgs('a', 'b', 'c')
print(str)

str2 = joinArgs('a', 'b', 'c', sep='.')
print(str2)