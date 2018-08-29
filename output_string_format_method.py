# 占位符
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# 占位符可以指定参数列表中的位置
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# 可以用关键字的形式来指定对应的参数
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

# 位置和关键字可以任意组合
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))

# 指定格式
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

# 另一种方式
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

for x in range(1, 11) :
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

