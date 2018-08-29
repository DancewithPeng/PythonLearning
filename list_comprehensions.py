# 列表推导
squares = []

# x在循环结束后会依然存在
for x in range(10) :
    squares.append(x**2)
print(squares)

# 更好的方式
squares2 = list(map(lambda x: x**2, range(10)))
print(squares2)

# 或者
squares3 = [x**2 for x in range(10)]
print(squares3)

# 列表推导语法，前面表示元素表达式，后面跟着多个for子句或者if子句，用于推导除表达式中的元素的值
squares4 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(squares4)

# 如果元素是元组，则必须用()括起来
vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

print([(x, x**2) for x in range(6)])

vec2 = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec2 for num in elem])

# 列表推导支持复杂的表达式和函数
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])


# 列表推导还可以嵌套
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

# 实际应用中应该用函数来代替复杂的流语句
print(list(zip(*matrix)))