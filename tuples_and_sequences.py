# 元组，用,分隔
t = 10086, '中国移动', 'cn'
print(t)
print(t[0])

# 元组，可以嵌套
u = t, 1, 2, 3
print(u)

# 元组是不可变的
#t[0] = 10010
#print(u)

# 但是可以包含可变的元素
tl = [1, 2, 3], [4, 5, 6]
tl[0][0] = 10010
print(tl)

# 空元组和单元素元组
empty = ()
singleton = 'hello', 
print(len(empty), empty)
print(len(singleton), singleton)

# 元组可以赋值
x, y, z = t
print(x, y, z)