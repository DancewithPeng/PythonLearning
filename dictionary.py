# 字典
tel = {'jack': 4098, 'sape': 4139}
print(tel['jack'])

# 赋值
tel['zhang'] = 2730
print(tel)

# 删除
del tel['sape']
print(tel)

# 根据字典key创建list
l = list(tel)
print(l)

# 对key进行排序
tel['abc'] = 10018
print(tel)
new = sorted(tel)
print(new)

# 判断是否包含某个元素
print('zhang' in tel)
print('zhang' not in tel)

# 通过元组序列来创建字典
d = dict([('name', 'zhangpeng'), ('age', 100), ('sex', 'man')])
print(d)

# 字典也支持推导语法
d2 = {x: x**2 for x in range(10)}
print(d2)

# 或者通过赋值的形式来创建
d3 = dict(zhang='peng', li = 'si', huang='wu') print(d3)
